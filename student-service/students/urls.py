from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KhoaViewSet, NganhDaoTaoViewSet, SinhVienViewSet

router = DefaultRouter()
router.register(r'khoa', KhoaViewSet)
router.register(r'nganh', NganhDaoTaoViewSet)
router.register(r'sinhvien', SinhVienViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/sinhvien/bulk-cdr-status/', bulk_cdr_status, name='bulk_cdr_status'),
]