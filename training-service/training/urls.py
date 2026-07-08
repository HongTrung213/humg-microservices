from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LopBoiDuongViewSet, DangKyLopViewSet

router = DefaultRouter()
router.register(r'lop', LopBoiDuongViewSet)
router.register(r'dangky', DangKyLopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]