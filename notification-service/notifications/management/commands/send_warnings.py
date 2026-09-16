import os
import logging
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from notifications.models import CanhBao, ThongBao
import requests

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'G?i c?nh báo cho sinh viên nam cu?i chua d?t CÐR'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Ch?y th?, không g?i th?c t?',
        )

    def get_access_token(self):
        """L?y token t? Gateway b?ng username/password admin"""
        try:
            auth_resp = requests.post(
                'http://localhost:8000/api/token/',
                json={'username': 'admin', 'password': os.getenv('ADMIN_PASSWORD')},
                timeout=5
            )
            if auth_resp.status_code == 200:
                return auth_resp.json().get('access')
            else:
                self.stdout.write(self.style.ERROR('Không th? l?y token t? Gateway'))
                return None
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'L?i k?t n?i Gateway: {e}'))
            return None

    def handle(self, *args, **options):
        dry_run = options.get('dry_run', False)
        self.stdout.write('B?t d?u ki?m tra sinh viên nam cu?i...')

        # L?y token
        token = self.get_access_token()
        if not token:
            return

        headers = {'Authorization': f'Bearer {token}'}

        # L?y danh sách sinh viên t? Student Service
        try:
            student_resp = requests.get(
                'http://localhost:8001/api/sinhvien/',
                headers=headers,
                timeout=5
            )
            if student_resp.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Không th? l?y danh sách sinh viên: {student_resp.text}'))
                return
            students = student_resp.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'L?i k?t n?i Student Service: {e}'))
            return

        # L?y danh sách d?t thi CÐR ngo?i ng?
        try:
            exam_resp = requests.get(
                'http://localhost:8002/api/lichsuthi/',
                headers=headers,
                timeout=5
            )
            if exam_resp.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Không th? l?y d? li?u thi: {exam_resp.text}'))
                return
            exams = exam_resp.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'L?i k?t n?i Exam Service: {e}'))
            return

        # L?c sinh viên nam cu?i (khoa_hoc K63 ho?c nam_nhap_hoc 2020)
        # D?a trên d? li?u th?c t?, di?u ch?nh di?u ki?n phù h?p
        final_year_students = [sv for sv in students if sv.get('khoa_hoc') in ['K63', 'K64', 'K65']]

        if not final_year_students:
            self.stdout.write(self.style.WARNING('Không tìm th?y sinh viên nam cu?i'))
            return

        self.stdout.write(f'Có {len(final_year_students)} sinh viên nam cu?i')

        # L?c nh?ng sinh viên chua d?t CÐR ngo?i ng?
        for sv in final_year_students:
            sinh_vien_id = sv.get('id')
            ma_sv = sv.get('ma_sv')
            ho_ten = sv.get('ho_ten')
            email = sv.get('email')

            # Ki?m tra CÐR ngo?i ng? (loai='CDR_NN' và dat=False)
            not_pass_nn = [e for e in exams if e.get('sinh_vien_id') == sinh_vien_id and e.get('mon_thi') == 'CDR_NGOAI_NGU' and e.get('ket_qua_dat') == False]
            if not_pass_nn:
                self.create_warning(sinh_vien_id, ma_sv, ho_ten, email, not_pass_nn, dry_run)

        self.stdout.write(self.style.SUCCESS('Hoàn t?t ki?m tra c?nh báo.'))

    def create_warning(self, sinh_vien_id, ma_sv, ho_ten, email, not_pass_list, dry_run):
        warning_title = f'C?nh báo: Chua d?t CÐR Ngo?i ng? - {ho_ten}'
        warning_content = f'Sinh viên {ho_ten} (MSSV: {ma_sv}) chua d?t CÐR ngo?i ng?.\n'
        for exam in not_pass_list:
            dot_thi = exam.get('dot_thi', {})
            ten_dot = dot_thi.get('ten_dot', '') if isinstance(dot_thi, dict) else str(dot_thi)
            diem = exam.get('diem', '')
            warning_content += f'  - Ð?t thi: {ten_dot} - Ði?m: {diem}\n'
        warning_content += 'Vui lòng dang ký thi l?i ho?c b?o luu di?m n?u d? di?u ki?n.'

        if dry_run:
            self.stdout.write(f'[DRY RUN] C?n g?i c?nh báo cho {ma_sv} ({ho_ten})')
            return

        # Luu vào DB (CanhBao) - gi? s? có model CanhBao
        CanhBao.objects.create(
            sinh_vien_id=sinh_vien_id,
            tieu_de=warning_title,
            noi_dung=warning_content,
            muc_do='HIGH',
            da_gui=False,
            ngay_gui=None
        )

        # G?i email (n?u có email)
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
                self.stdout.write(self.style.SUCCESS(f'Ðã g?i email d?n {email}'))
            except Exception as e:
                logger.error(f'Không th? g?i email d?n {email}: {e}')

        self.stdout.write(self.style.SUCCESS(f'Ðã t?o c?nh báo cho {ma_sv}'))
