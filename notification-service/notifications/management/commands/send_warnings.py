import os
import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from notifications.models import CanhBao, ThongBao
import requests

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Gửi cảnh báo cho sinh viên năm cuối chưa đạt CĐR'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Chạy thử, không gửi thực tế',
        )

    def get_access_token(self):
        """Lấy token từ Gateway bằng username/password admin"""
        try:
            auth_resp = requests.post(
                'http://localhost:8000/api/token/',
                json={'username': 'admin', 'password': '123qwe'},
                timeout=5
            )
            if auth_resp.status_code == 200:
                return auth_resp.json().get('access')
            else:
                self.stdout.write(self.style.ERROR('Không thể lấy token từ Gateway'))
                return None
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Lỗi kết nối Gateway: {e}'))
            return None

    def handle(self, *args, **options):
        dry_run = options.get('dry_run', False)
        self.stdout.write('Bắt đầu kiểm tra sinh viên năm cuối...')

        # Lấy token
        token = self.get_access_token()
        if not token:
            return

        headers = {'Authorization': f'Bearer {token}'}

        # Lấy danh sách sinh viên từ Student Service
        try:
            student_resp = requests.get(
                'http://localhost:8001/api/sinhvien/',
                headers=headers,
                timeout=5
            )
            if student_resp.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Không thể lấy danh sách sinh viên: {student_resp.text}'))
                return
            students = student_resp.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Lỗi kết nối Student Service: {e}'))
            return

        # Lấy danh sách đợt thi CĐR ngoại ngữ
        try:
            exam_resp = requests.get(
                'http://localhost:8002/api/lichsuthi/',
                headers=headers,
                timeout=5
            )
            if exam_resp.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Không thể lấy dữ liệu thi: {exam_resp.text}'))
                return
            exams = exam_resp.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Lỗi kết nối Exam Service: {e}'))
            return

        # Lọc sinh viên năm cuối (khoa_hoc K63 hoặc nam_nhap_hoc 2020)
        # Dựa trên dữ liệu thực tế, điều chỉnh điều kiện phù hợp
        final_year_students = [sv for sv in students if sv.get('khoa_hoc') in ['K63', 'K64', 'K65']]

        if not final_year_students:
            self.stdout.write(self.style.WARNING('Không tìm thấy sinh viên năm cuối'))
            return

        self.stdout.write(f'Có {len(final_year_students)} sinh viên năm cuối')

        # Lọc những sinh viên chưa đạt CĐR ngoại ngữ
        for sv in final_year_students:
            sinh_vien_id = sv.get('id')
            ma_sv = sv.get('ma_sv')
            ho_ten = sv.get('ho_ten')
            email = sv.get('email')

            # Kiểm tra CĐR ngoại ngữ (loai='CDR_NN' và dat=False)
            not_pass_nn = [e for e in exams if e.get('sinh_vien_id') == sinh_vien_id and e.get('loai') == 'CDR_NN' and e.get('dat') == False]

            if not_pass_nn:
                self.create_warning(sinh_vien_id, ma_sv, ho_ten, email, not_pass_nn, dry_run)

        self.stdout.write(self.style.SUCCESS('Hoàn tất kiểm tra cảnh báo.'))

    def create_warning(self, sinh_vien_id, ma_sv, ho_ten, email, not_pass_list, dry_run):
        warning_title = f'Cảnh báo: Chưa đạt CĐR Ngoại ngữ - {ho_ten}'
        warning_content = f'Sinh viên {ho_ten} (MSSV: {ma_sv}) chưa đạt CĐR ngoại ngữ.\n'
        for exam in not_pass_list:
            dot_thi = exam.get('dot_thi', {})
            ten_dot = dot_thi.get('ten_dot', '') if isinstance(dot_thi, dict) else str(dot_thi)
            diem = exam.get('diem', '')
            warning_content += f'  - Đợt thi: {ten_dot} - Điểm: {diem}\n'
        warning_content += 'Vui lòng đăng ký thi lại hoặc bảo lưu điểm nếu đủ điều kiện.'

        if dry_run:
            self.stdout.write(f'[DRY RUN] Cần gửi cảnh báo cho {ma_sv} ({ho_ten})')
            return

        # Lưu vào DB (CanhBao) - giả sử có model CanhBao
        CanhBao.objects.create(
            sinh_vien_id=sinh_vien_id,
            tieu_de=warning_title,
            noi_dung=warning_content,
            muc_do='HIGH',
            da_gui=False,
            ngay_gui=None
        )

        # Gửi email (nếu có email)
        if email:
            try:
                from django.core.mail import send_mail
                send_mail(
                    warning_title,
                    warning_content,
                    'no-reply@humg.edu.vn',
                    [email],
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(f'Đã gửi email đến {email}'))
            except Exception as e:
                logger.error(f'Không thể gửi email đến {email}: {e}')

        self.stdout.write(self.style.SUCCESS(f'Đã tạo cảnh báo cho {ma_sv}'))