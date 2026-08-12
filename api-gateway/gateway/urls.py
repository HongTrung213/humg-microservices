from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views as gateway_views

app_name = 'admin_mofi'  # Namespace cho admin

urlpatterns = [
    # --- JWT Authentication ---
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/', include('proxy.urls')),  # Proxy các service backend

    # ===================================================
    # GIAO DIỆN ADMIN (namespace: admin_mofi)
    # ===================================================

    # Dashboard
    path('admin/dashboard/', gateway_views.admin_mofi_dashboard, name='admin_dashboard'),
    path('admin/report-dashboard/', gateway_views.admin_mofi_dashboard, name='admin_mofi_dashboard'),

    # Quản lý sinh viên
#     path('admin/students/', gateway_views.student_list, name='student_list'),
#     path('admin/students/add/', gateway_views.student_create, name='student_add'),
#     path('admin/students/<int:student_id>/', gateway_views.student_detail, name='student_detail'),
#     path('admin/students/<int:student_id>/edit/', gateway_views.student_edit, name='student_edit'),
    path('admin/students/import/', gateway_views.import_excel_student, name='import_excel_student'),

    # Quản lý khoa, ngành
    path('admin/khoa/', gateway_views.khoa_list, name='khoa_list'),
    path('admin/khoa/add/', gateway_views.khoa_create, name='khoa_add'),
    path('admin/khoa/<int:pk>/edit/', gateway_views.khoa_edit, name='khoa_edit'),
    path('admin/khoa/<int:pk>/delete/', gateway_views.khoa_delete, name='khoa_delete'),
    path('admin/nganh/', gateway_views.nganh_list, name='nganh_list'),
    path('admin/nganh/add/', gateway_views.nganh_create, name='nganh_add'),
    path('admin/nganh/<int:pk>/edit/', gateway_views.nganh_edit, name='nganh_edit'),
    path('admin/nganh/<int:pk>/delete/', gateway_views.nganh_delete, name='nganh_delete'),

    # Quản lý danh mục chứng chỉ
    path('admin/chungchi/', gateway_views.chungchi_list, name='chungchi_list'),
    path('admin/chungchi/add/', gateway_views.chungchi_create, name='chungchi_add'),
    path('admin/chungchi/<int:pk>/edit/', gateway_views.chungchi_edit, name='chungchi_edit'),
    path('admin/chungchi/<int:pk>/delete/', gateway_views.chungchi_delete, name='chungchi_delete'),

    # Tiêu chí CĐR
    path('admin/tieu-chi/', gateway_views.tieu_chi_list, name='tieu_chi_list'),

    # Quản lý đợt thi
    path('admin/dot-thi/', gateway_views.dot_thi_list, name='dot_thi_list'),
    path('admin/dot-thi/create/', gateway_views.dot_thi_create, name='dot_thi_create'),
    path('admin/dot-thi/<int:pk>/', gateway_views.dot_thi_detail, name='dot_thi_detail'),

    # Import dữ liệu (Excel)
    path('admin/import/lich-thi-tdnn/', gateway_views.import_exam_data, {'loai': 'lich_thi_tdnn'}, name='import_lich_thi_tdnn'),
    path('admin/import/lich-thi-nn/', gateway_views.import_exam_data, {'loai': 'lich_thi_nn'}, name='import_lich_thi_nn'),
    path('admin/import/lich-thi-cntt/', gateway_views.import_exam_data, {'loai': 'lich_thi_cntt'}, name='import_lich_thi_cntt'),
    path('admin/import/diem-tdnn/', gateway_views.import_exam_data, {'loai': 'diem_tdnn'}, name='import_diem_tdnn'),
    path('admin/import/diem-cdr-nn/', gateway_views.import_exam_data, {'loai': 'diem_cdr_nn'}, name='import_diem_cdr_nn'),
    path('admin/import/diem-cntt/', gateway_views.import_exam_data, {'loai': 'diem_cntt'}, name='import_diem_cntt'),

    # Quản lý lớp bồi dưỡng
    path('admin/classes/', gateway_views.class_list, name='class_list'),
    path('admin/classes/add/', gateway_views.class_create, name='class_add'),
    path('admin/classes/<int:pk>/edit/', gateway_views.class_edit, name='class_edit'),
    path('admin/classes/<int:pk>/delete/', gateway_views.class_delete, name='class_delete'),
    path('admin/classes/import/', gateway_views.import_class_list, name='import_class_list'),

    # Quản lý CMS (bài viết, danh mục, slider, quicklink)
    path('admin/posts/', gateway_views.post_list, name='post_list'),
    path('admin/posts/add/', gateway_views.post_create, name='post_add'),
    path('admin/posts/<int:pk>/edit/', gateway_views.post_edit, name='post_edit'),
    path('admin/posts/<int:pk>/delete/', gateway_views.post_delete, name='post_delete'),
    path('admin/categories/', gateway_views.category_list, name='category_list'),
    path('admin/categories/add/', gateway_views.category_create, name='category_add'),
    path('admin/categories/<int:pk>/edit/', gateway_views.category_edit, name='category_edit'),
    path('admin/categories/<int:pk>/delete/', gateway_views.category_delete, name='category_delete'),
    path('admin/sliders/', gateway_views.slider_list, name='slider_list'),
    path('admin/sliders/add/', gateway_views.slider_create, name='slider_add'),
    path('admin/sliders/<int:pk>/edit/', gateway_views.slider_edit, name='slider_edit'),
    path('admin/sliders/<int:pk>/delete/', gateway_views.slider_delete, name='slider_delete'),
    path('admin/quicklinks/', gateway_views.quicklink_list, name='quicklink_list'),
    path('admin/quicklinks/add/', gateway_views.quicklink_create, name='quicklink_add'),
    path('admin/quicklinks/<int:pk>/edit/', gateway_views.quicklink_edit, name='quicklink_edit'),
    path('admin/quicklinks/<int:pk>/delete/', gateway_views.quicklink_delete, name='quicklink_delete'),

    # Quản lý thông báo
    path('admin/thongbao/', gateway_views.thongbao_list, name='thongbao_list'),
    path('admin/thongbao/add/', gateway_views.thongbao_create, name='thongbao_add'),
    path('admin/thongbao/<int:pk>/edit/', gateway_views.thongbao_edit, name='thongbao_edit'),
    path('admin/thongbao/<int:pk>/delete/', gateway_views.thongbao_delete, name='thongbao_delete'),

    # Quản lý tài khoản và nhóm quyền (Django Auth)
    path('admin/users/', gateway_views.user_list, name='user_list'),
    path('admin/users/add/', gateway_views.user_create, name='user_add'),
    path('admin/users/<int:pk>/edit/', gateway_views.user_edit, name='user_edit'),
    path('admin/groups/', gateway_views.group_list, name='group_list'),
    path('admin/groups/add/', gateway_views.group_create, name='group_add'),
    path('admin/groups/<int:pk>/edit/', gateway_views.group_edit, name='group_edit'),

    # ===================================================
    # GIAO DIỆN PORTAL (students/)
    # ===================================================
    path('admin/classes/<int:pk>/import-students/', gateway_views.import_class_students, name='import_class_students'),
    path('admin/classes/<int:pk>/import-schedule/', gateway_views.import_class_schedule, name='import_class_schedule'),

    # Include portal URLs
    path('', include('gateway.portal_urls')),
]

# Thêm đường dẫn cho static và media files (nếu có)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
