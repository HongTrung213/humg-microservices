from django.urls import path
from . import views as gateway_views

app_name = 'students'

urlpatterns = [
    path('', gateway_views.home, name='home'),
    path('dashboard/', gateway_views.student_dashboard, name='dashboard'),
    path('tra-cuu/', gateway_views.tra_cuu, name='tra_cuu'),
    path('dang-nhap/', gateway_views.dang_nhap, name='dang_nhap'),
    path('dang-xuat/', gateway_views.dang_xuat, name='dang_xuat'),
    path('quy-che/', gateway_views.quy_che_list, name='quy_che_list'),
    path('quy-che/<slug:slug>/', gateway_views.quy_che_detail, name='quy_che_detail'),
    # Các route t?m th?i tr? v? home d? tránh l?i (có th? tách view riêng sau)
    path('khoa-hoc/', gateway_views.home, name='khoa_hoc'),
    path('khoa-hoc-ngoai-ngu/', gateway_views.home, name='khoa_hoc_ngoai_ngu'),
    path('khoa-hoc-tin-hoc/', gateway_views.home, name='khoa_hoc_tin_hoc'),
    path('lich-hoc-lich-thi/', gateway_views.home, name='lich_hoc_lich_thi'),
    path('tin-tuc/', gateway_views.home, name='tin_tuc'),
    path('huong-dan-dang-ky/', gateway_views.home, name='huong_dan_dang_ky'),
    path('lien-he/', gateway_views.home, name='lien_he'),
    path('tu-van-ho-tro/', gateway_views.home, name='tu_van_ho_tro'),
    path('chung-chi-cntt/', gateway_views.home, name='chung_chi_cntt'),
    path('chung-chi-ngoai-ngu/', gateway_views.home, name='chung_chi_ngoai_ngu'),

    path('home/', gateway_views.home, name='home'),

    path('dashboard/', gateway_views.home, name='dashboard'),

    path('tra-cuu/', gateway_views.home, name='tra_cuu'),

    path('dang-nhap/', gateway_views.home, name='dang_nhap'),

    path('dang-xuat/', gateway_views.home, name='dang_xuat'),

    path('quy-che-list/', gateway_views.home, name='quy_che_list'),

    path('quy-che-detail/', gateway_views.home, name='quy_che_detail'),

    path('tieng-anh-tang-cuong/', gateway_views.home, name='tieng_anh_tang_cuong'),

    path('on-luyen-chuan-dau-ra-ngoai-ngu/', gateway_views.home, name='on_luyen_chuan_dau_ra_ngoai_ngu'),

    path('on-luyen-chuan-dau-ra-cntt/', gateway_views.home, name='on_luyen_chuan_dau_ra_cntt'),

    path('chung-chi-ung-dung-cntt/', gateway_views.home, name='chung_chi_ung_dung_cntt'),

    path('dang-ky-tu-van/', gateway_views.home, name='dang_ky_tu_van'),

    path('lich-thi/', gateway_views.home, name='lich_thi'),

    path('quy-che/', gateway_views.home, name='quy_che'),

    path('nop-chung-chi/', gateway_views.home, name='nop_chung_chi'),
]
