from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KhoaViewSet, NganhDaoTaoViewSet, SinhVienViewSet
from .views import import_students, bulk_cdr_status   # thêm bulk_cdr_status

router = DefaultRouter()
router.register(r'khoa', KhoaViewSet)
router.register(r'nganh', NganhDaoTaoViewSet)
router.register(r'sinhvien', SinhVienViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('import-students/', import_students, name='import_students'),   # đã có
    path('sinhvien/bulk-cdr-status/', bulk_cdr_status, name='bulk_cdr_status'),  # thêm
]
