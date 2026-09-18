# -*- coding: utf-8 -*-
"""Seed 10 Khoa + 53 Nganh cho HUMG."""
from django.core.management.base import BaseCommand
from django.db import transaction
from students.models import Khoa, NganhDaoTao


DEFAULT_KHOA = [
    ('100', 'Khoa Khoa học cơ bản'),
    ('101', 'Khoa Dầu khí'),
    ('102', 'Khoa Địa chất'),
    ('103', 'Khoa Trắc địa - Bản đồ và Quản lý đất đai'),
    ('104', 'Khoa Mỏ'),
    ('105', 'Khoa Công nghệ Thông tin'),
    ('106', 'Khoa Cơ - Điện'),
    ('107', 'Khoa Xây dựng'),
    ('108', 'Khoa Môi trường'),
    ('401', 'Khoa Kinh tế - Quản trị Kinh doanh'),
]


DEFAULT_NGANH = [
    # Khoa Dau khi (101)
    ('7440229', 'Quản lý và phân tích dữ liệu khoa học trái đất', '101', 'THUONG', 4.0),
    ('7510401', 'Công nghệ kỹ thuật hóa học', '101', 'THUONG', 4.5),
    ('7520502', 'Kỹ thuật địa vật lý', '101', 'THUONG', 4.5),
    ('7520604', 'Kỹ thuật dầu khí', '101', 'THUONG', 5.0),
    ('7520605', 'Kỹ thuật khí thiên nhiên', '101', 'THUONG', 5.0),
    ('7520606', 'Công nghệ số trong thăm dò và khai thác tài nguyên thiên nhiên', '101', 'THUONG', 4.5),
    ('7520301', 'Kỹ thuật hoá học', '101', 'THUONG', 4.5),
    ('7520301TL', 'Kỹ thuật hoá học Chương trình tiên tiến', '101', 'THUONG', 4.5),
    # Khoa Mo (104)
    ('7520601', 'Kỹ thuật mỏ', '104', 'THUONG', 4.5),
    ('7520607', 'Kỹ thuật tuyển khoáng', '104', 'THUONG', 4.5),
    ('7850202', 'An toàn, Vệ sinh lao động', '104', 'THUONG', 4.0),
    ('7520601TL', 'Kỹ thuật mỏ thông minh', '104', 'THUONG', 4.5),
    # Khoa KH Co ban (100)
    ('7510402', 'Công nghệ vật liệu', '100', 'THUONG', 4.5),
    ('7720203', 'Hóa dược', '100', 'THUONG', 4.5),
    ('7520309', 'Kỹ thuật vật liệu', '100', 'THUONG', 4.5),
    ('7220201', 'Ngôn ngữ Anh', '100', 'NGON_NGU_ANH', 4.0),
    ('7220204', 'Ngôn ngữ Trung Quốc', '100', 'NGON_NGU_TRUNG', 4.0),
    # Khoa Trac dia (103)
    ('7480206', 'Địa tin học', '103', 'THUONG', 4.5),
    ('7520121', 'Kỹ thuật không gian', '103', 'THUONG', 4.5),
    ('7520503', 'Kỹ thuật trắc địa - bản đồ', '103', 'THUONG', 4.5),
    ('7850103', 'Quản lý đất đai', '103', 'THUONG', 4.0),
    ('7580109', 'Quản lý phát triển đô thị và bất động sản', '103', 'THUONG', 4.0),
    # Khoa Moi truong (108)
    ('7520320', 'Kỹ thuật môi trường', '108', 'THUONG', 4.5),
    ('7850101', 'Quản lý tài nguyên và môi trường', '108', 'THUONG', 4.0),
    # Khoa Kinh te (401)
    ('7340101', 'Quản trị kinh doanh', '401', 'THUONG', 4.0),
    ('7340301', 'Kế toán', '401', 'THUONG', 4.0),
    ('7340201', 'Tài chính - Ngân hàng', '401', 'THUONG', 4.0),
    ('7510601', 'Quản lý công nghiệp', '401', 'THUONG', 4.0),
    # Khoa CNTT (105)
    ('7480201', 'Công nghệ thông tin', '105', 'THUONG', 4.5),
    ('7460108', 'Khoa học dữ liệu', '105', 'THUONG', 4.0),
    ('7480201TL', 'Trí tuệ nhân tạo ứng dụng và bản sao số trái đất', '105', 'THUONG', 4.5),
    # Khoa Xay dung (107)
    ('7580201', 'Kỹ thuật xây dựng', '107', 'THUONG', 4.5),
    ('7580205', 'Kỹ thuật xây dựng công trình giao thông', '107', 'THUONG', 4.5),
    ('7580204', 'Xây dựng công trình ngầm thành phố và Hệ thống tàu điện ngầm', '107', 'THUONG', 4.5),
    ('7580302', 'Quản lý xây dựng', '107', 'THUONG', 4.5),
    ('7580201TL', 'Kỹ thuật xây dựng công trình ngầm', '107', 'THUONG', 4.5),
    # Khoa Co - Dien (106)
    ('7510301', 'Công nghệ kỹ thuật điện, điện tử', '106', 'THUONG', 4.5),
    ('7520103', 'Kỹ thuật cơ khí', '106', 'THUONG', 4.5),
    ('7520114', 'Kỹ thuật cơ điện tử', '106', 'THUONG', 4.5),
    ('7520116', 'Kỹ thuật cơ khí động lực', '106', 'THUONG', 4.5),
    ('7520130', 'Kỹ thuật ô tô', '106', 'THUONG', 4.5),
    ('7520201', 'Kỹ thuật điện', '106', 'THUONG', 4.5),
    ('7520216', 'Kỹ thuật điều khiển và tự động hóa', '106', 'THUONG', 4.5),
    ('7520107', 'Kỹ thuật Robot', '106', 'THUONG', 4.5),
    ('7520216TL', 'Kỹ thuật điều khiển và tự động hóa phục vụ công nghiệp khai khoáng và năng lượng', '106', 'THUONG', 4.5),
    # Khoa Dia chat (102)
    ('7520501', 'Kỹ thuật địa chất', '102', 'THUONG', 4.5),
    ('7850196', 'Quản lý tài nguyên khoáng sản', '102', 'THUONG', 4.0),
    ('7580106', 'Quản lý đô thị và công trình', '102', 'THUONG', 4.0),
    ('7580211', 'Địa kỹ thuật xây dựng', '102', 'THUONG', 4.5),
    ('7580212', 'Kỹ thuật tài nguyên nước', '102', 'THUONG', 4.5),
    ('7440201', 'Địa chất học', '102', 'THUONG', 4.5),
    ('7810105', 'Du lịch địa chất', '102', 'THUONG', 4.0),
    ('7520505', 'Đá quý Đá mỹ nghệ', '102', 'THUONG', 4.5),
    ('7520501TL', 'Kỹ thuật địa chất phục vụ công nghiệp đất hiếm và khoáng sản chiến lược', '102', 'THUONG', 4.5),
]


class Command(BaseCommand):
    help = 'Seed 10 Khoa + 53 Nganh cho HUMG.'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Xoa het truoc khi seed.')

    @transaction.atomic
    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write(self.style.WARNING('Xoa het Khoa + Nganh...'))
            NganhDaoTao.objects.all().delete()
            Khoa.objects.all().delete()

        # Seed Khoa
        khoa_map = {}
        ck = 0
        for ma, ten in DEFAULT_KHOA:
            obj, created = Khoa.objects.get_or_create(ma_khoa=ma, defaults={'ten_khoa': ten})
            khoa_map[ma] = obj
            if created:
                ck += 1
        self.stdout.write(self.style.SUCCESS(f'[KHOA] Tao moi: {ck}, Tong: {len(DEFAULT_KHOA)}'))

        # Seed Nganh
        cn = 0
        un = 0
        for ma_nganh, ten, ma_khoa, loai, so_nam in DEFAULT_NGANH:
            khoa = khoa_map.get(ma_khoa)
            if not khoa:
                self.stdout.write(self.style.WARNING(f'[SKIP] {ten} - khong co khoa {ma_khoa}'))
                continue
            obj = NganhDaoTao.objects.filter(khoa=khoa, ten_nganh=ten).first()
            if obj:
                changed = []
                if obj.ma_nganh != ma_nganh:
                    obj.ma_nganh = ma_nganh
                    changed.append('ma_nganh')
                if obj.loai_nganh != loai:
                    obj.loai_nganh = loai
                    changed.append('loai_nganh')
                if obj.thoi_gian_dao_tao_nam != so_nam:
                    obj.thoi_gian_dao_tao_nam = so_nam
                    changed.append('thoi_gian_dao_tao_nam')
                if not obj.is_active:
                    obj.is_active = True
                    changed.append('is_active')
                if changed:
                    obj.save(update_fields=changed)
                    un += 1
            else:
                NganhDaoTao.objects.create(
                    ma_nganh=ma_nganh, ten_nganh=ten, khoa=khoa,
                    loai_nganh=loai, thoi_gian_dao_tao_nam=so_nam, is_active=True,
                )
                cn += 1
        self.stdout.write(self.style.SUCCESS(f'[NGANH] Tao moi: {cn}, Cap nhat: {un}, Tong: {len(DEFAULT_NGANH)}'))
        self.stdout.write(self.style.SUCCESS(f'\n== HOAN TAT == Khoa: {Khoa.objects.count()}, Nganh: {NganhDaoTao.objects.count()}'))
