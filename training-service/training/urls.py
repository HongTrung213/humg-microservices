from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LopBoiDuongViewSet, DangKyLopViewSet, LichHocViewSet

router = DefaultRouter()
router.register(r'lop', LopBoiDuongViewSet)
router.register(r'dangky', DangKyLopViewSet)
router.register(r'lich-hoc', LichHocViewSet)  # Thêm router mới

urlpatterns = [
    path('', include(router.urls)),
]