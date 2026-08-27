from django.core.management.base import BaseCommand
from exams.utils.bao_luu_utils import kiem_tra_bao_luu_het_han

class Command(BaseCommand):
    help = 'Kiểm tra và cập nhật bảo lưu điểm hết hạn'

    def handle(self, *args, **options):
        count = kiem_tra_bao_luu_het_han()
        self.stdout.write(f'Đã cập nhật {count} bảo lưu hết hạn')
