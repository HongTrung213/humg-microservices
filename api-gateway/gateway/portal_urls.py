from django.urls import path
from . import views as gateway_views

app_name = 'students'

urlpatterns = [
    # Trang chính
    path('', gateway_views.home, name='home'),
    path('dashboard/', gateway_views.student_dashboard, name='dashboard'),
    path('tra-cuu/', gateway_views.tra_cuu, name='tra_cuu'),
    path('dang-nhap/', gateway_views.dang_nhap, name='dang_nhap'),
    path('dang-xuat/', gateway_views.dang_xuat, name='dang_xuat'),

    # Quy chế - Văn bản
    path('quy-che/', gateway_views.quy_che_list, name='quy_che_list'),
    path('quy-che/<slug:slug>/', gateway_views.quy_che_detail, name='quy_che_detail'),

    # Chứng chỉ
    path('nop-chung-chi/', gateway_views.nop_chung_chi, name='nop_chung_chi'),
    path('cert/add/', gateway_views.quick_add_cert_portal, name='quick_add_cert_portal'),
    path('cert/<int:cert_id>/delete/', gateway_views.student_delete_cert, name='student_delete_cert'),

    # Tin tức / CMS
    path('tin-tuc/', gateway_views.post_list_portal, name='post_list'),
    path('tin-tuc/<slug:slug>/', gateway_views.post_detail, name='post_detail'),
    path('tin-tuc/danh-muc/<slug:slug>/', gateway_views.post_list_by_category, name='post_list_by_category'),

    # Lớp bồi dưỡng
    path('danh-sach-lop/', gateway_views.danh_sach_lop, name='danh_sach_lop'),

    # Lịch thi (tạm)
    path('lich-thi/', gateway_views.home, name='lich_thi'),

    # Profile
    path('dashboard/profile/', gateway_views.student_profile, name='student_profile'),
]