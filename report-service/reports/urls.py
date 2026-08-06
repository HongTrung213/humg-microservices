from django.urls import path
from .views import (
    thong_ke_sinh_vien,
    thong_ke_thi,
    dashboard_stats,
    chua_dat_chuan,
    export_chua_dat_chuan,
    thong_ke_theo_khoa,
    lich_su_thi_sinh_vien,
    thong_ke_tien_do_cdr,
    thong_ke_diem_theo_thoi_gian,
    thong_ke_sv_theo_nhom,
    thong_ke_bao_luu,
)

urlpatterns = [
    # Các API hiện có
    path('thong-ke-sv/', thong_ke_sinh_vien, name='thong_ke_sinh_vien'),
    path('thong-ke-thi/', thong_ke_thi, name='thong_ke_thi'),
    
    # API mới (dashboard, báo cáo)
    path('dashboard/', dashboard_stats, name='dashboard_stats'),
    path('chua-dat-chuan/', chua_dat_chuan, name='chua_dat_chuan'),
    path('export-chua-dat-chuan/', export_chua_dat_chuan, name='export_chua_dat_chuan'),
    path('thong-ke-theo-khoa/', thong_ke_theo_khoa, name='thong_ke_theo_khoa'),
    path('lich-su-thi/<int:sinh_vien_id>/', lich_su_thi_sinh_vien, name='lich_su_thi_sinh_vien'),
    
    # ===== API TÍNH TOÁN MỚI =====
    path('tien-do-cdr/', thong_ke_tien_do_cdr, name='thong_ke_tien_do_cdr'),
    path('diem-theo-thoi-gian/', thong_ke_diem_theo_thoi_gian, name='thong_ke_diem_theo_thoi_gian'),
    path('sv-theo-nhom/', thong_ke_sv_theo_nhom, name='thong_ke_sv_theo_nhom'),
    path('bao-luu/', thong_ke_bao_luu, name='thong_ke_bao_luu'),
]