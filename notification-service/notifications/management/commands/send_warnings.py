# -*- coding: utf-8 -*-
"""
Gửi cảnh báo cho sinh viên năm cuối chưa đạt CĐR.

- Gọi bulk-cdr-status của student-service để lấy CĐR đã tính sẵn
  (đã bao gồm cả điểm thi + chứng chỉ)
- Dedupe: bỏ qua nếu đã gửi cảnh báo trong N ngày
- Email: dùng email_truong fallback email_ca_nhan
- Cho phép override mã khóa qua --khoa-hoc
"""
import os
import logging
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from notifications.models import CanhBao
import requests

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Gửi cảnh báo cho sinh viên năm cuối chưa đạt CĐR'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true',
                            help='Chạy thử, không gửi thực tế')
        parser.add_argument('--skip-email', action='store_true',
                            help='Chỉ tạo CanhBao, không gửi email')
        parser.add_argument('--dedupe-days', type=int, default=7,
                            help='Số ngày để dedupe (mặc định 7)')
        parser.add_argument('--khoa-hoc', type=str, default=None,
                            help='Override mã khóa (VD: K70,K71).')
        parser.add_argument('--khoa-id', type=int, default=None,
                            help='Lọc theo khoa_id (tuỳ chọn)')

    def get_access_token(self):
        """Lấy JWT token từ gateway."""
        pwd = os.getenv('ADMIN_PASSWORD')
        if not pwd:
            self.stdout.write(self.style.ERROR('Thiếu ADMIN_PASSWORD env'))
            return None

        gateway_url = os.getenv('GATEWAY_URL', 'http://localhost:8000')

        try:
            resp = requests.post(
                f'{gateway_url}/api/token/',
                json={'username': 'admin', 'password': pwd},
                timeout=5,
            )
            if resp.status_code == 200:
                return resp.json().get('access')
            self.stdout.write(self.style.ERROR(
                f'Không lấy được token: HTTP {resp.status_code}'
            ))
            return None
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Lỗi kết nối gateway: {e}'))
            return None

    def get_final_year_codes(self, override=None):
        """Xác định mã khóa cần cảnh báo."""
        if override:
            return [c.strip() for c in override.split(',') if c.strip()]

        nam_hien_tai = timezone.now().year
        return [f'K{str(y)[-2:]}' for y in range(nam_hien_tai - 5, nam_hien_tai - 3)]

    def fetch_cdr_status(self, headers):
        """
        Gọi bulk-cdr-status để lấy CĐR của TẤT CẢ sinh viên.
        Endpoint này đã check cả điểm thi + chứng chỉ.
        """
        student_url = os.getenv('STUDENT_SERVICE_URL', 'http://localhost:8001')

        try:
            resp = requests.get(
                f'{student_url}/api/sinhvien/bulk-cdr-status/',
                headers=headers,
                timeout=60,
            )
            if resp.status_code != 200:
                self.stdout.write(self.style.ERROR(
                    f'bulk-cdr-status trả HTTP {resp.status_code}'
                ))
                return None

            data = resp.json()
            if isinstance(data, dict):
                return data.get('results', [])
            return data or []
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Lỗi SV service: {e}'))
            return None

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        skip_email = options['skip_email']
        dedupe_days = options['dedupe_days']
        khoa_hoc_override = options.get('khoa_hoc')
        khoa_id_filter = options.get('khoa_id')

        self.stdout.write('Bắt đầu kiểm tra sinh viên năm cuối...')

        token = self.get_access_token()
        if not token:
            return

        headers = {'Authorization': f'Bearer {token}'}

        # 1. Lấy CĐR (đã tính sẵn cả exam + cert)
        cdr_results = self.fetch_cdr_status(headers)
        if cdr_results is None:
            return

        if not cdr_results:
            self.stdout.write(self.style.WARNING('Không có dữ liệu CĐR'))
            return

        self.stdout.write(f'Tổng SV có CĐR status: {len(cdr_results)}')

        # 2. Filter theo khoa_hoc và khoa_id
        final_year_codes = self.get_final_year_codes(khoa_hoc_override)
        self.stdout.write(f'Mã khóa cần cảnh báo: {final_year_codes}')

        filtered = []
        for sv in cdr_results:
            khoa_hoc = sv.get('khoa_hoc', '')
            if khoa_hoc not in final_year_codes:
                continue
            if khoa_id_filter and sv.get('khoa_id') != khoa_id_filter:
                continue
            filtered.append(sv)

        if not filtered:
            self.stdout.write(self.style.WARNING(
                f'Không tìm thấy SV với khoa_hoc trong {final_year_codes}'
            ))
            self.stdout.write('Gợi ý: dùng --khoa-hoc K70 để test')
            return

        self.stdout.write(f'Có {len(filtered)} SV năm cuối')

        # 3. Lọc SV chưa đạt CĐR NN
        sent = 0
        skipped_dupe = 0
        passed = 0

        cutoff = timezone.now() - timedelta(days=dedupe_days)

        for sv in filtered:
            sv_id = sv.get('id')
            ma_sv = sv.get('ma_sv', '')
            ho_ten = sv.get('ho_ten', '')
            email = sv.get('email_truong') or sv.get('email_ca_nhan') or ''

            # CĐR đã tính sẵn bên student-service (đã check exam + cert)
            dat_nn = sv.get('check_dat_ngoai_ngu', False)

            if dat_nn:
                passed += 1
                self.stdout.write(self.style.SUCCESS(
                    f'  [SKIP] {ma_sv} đã đạt NN'
                ))
                continue

            # Dedupe
            da_canh_bao = CanhBao.objects.filter(
                sinh_vien_id=sv_id,
                tieu_de__contains='CDR Ngoại ngữ',
                ngay_gui__gte=cutoff,
            ).exists()

            if da_canh_bao:
                skipped_dupe += 1
                self.stdout.write(
                    f'  [DEDUPE] {ma_sv} đã cảnh báo trong {dedupe_days} ngày'
                )
                continue

            if self.create_warning(sv_id, ma_sv, ho_ten, email,
                                    dry_run, skip_email):
                sent += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nHoàn tất! Gửi: {sent}, Bỏ qua (đã đạt): {passed}, '
            f'Bỏ qua (dedupe): {skipped_dupe}'
        ))

    def create_warning(self, sv_id, ma_sv, ho_ten, email,
                        dry_run, skip_email):
        """Tạo cảnh báo + gửi email."""
        warning_title = 'Cảnh báo: Chưa đạt CDR Ngoại ngữ'
        warning_content = (
            f'Sinh viên {ho_ten} (MSSV: {ma_sv}) chưa đạt CDR Ngoại ngữ.\n\n'
            f'Vui lòng đăng ký thi lại hoặc nộp chứng chỉ quốc tế.'
        )

        if dry_run:
            self.stdout.write(f'  [DRY RUN] Sẽ gửi cho {ma_sv} ({ho_ten})')
            return True

        try:
            cb = CanhBao.objects.create(
                sinh_vien_id=sv_id,
                tieu_de=warning_title,
                noi_dung=warning_content,
                muc_do='HIGH',
                da_gui=False,
                ngay_gui=None,
            )
        except Exception as e:
            logger.error(f'Không tạo được CanhBao cho {ma_sv}: {e}')
            return False

        if email and not skip_email:
            try:
                send_mail(
                    warning_title,
                    warning_content,
                    getattr(settings, 'DEFAULT_FROM_EMAIL', 'no-reply@humg.edu.vn'),
                    [email],
                    fail_silently=False,
                )
                cb.da_gui = True
                cb.ngay_gui = timezone.now()
                cb.save(update_fields=['da_gui', 'ngay_gui'])
                self.stdout.write(self.style.SUCCESS(
                    f'  ✅ Đã gửi cho {ma_sv} ({email})'
                ))
            except Exception as e:
                logger.error(f'Không gửi được email cho {ma_sv}: {e}')
                self.stdout.write(self.style.WARNING(
                    f'  ⚠️ Đã tạo CanhBao nhưng không gửi được email cho {ma_sv}'
                ))
        else:
            self.stdout.write(self.style.SUCCESS(
                f'  ✅ Đã tạo cảnh báo cho {ma_sv}'
            ))

        return True