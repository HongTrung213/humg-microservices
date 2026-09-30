from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BaiVietViewSet,
    SliderViewSet,
    QuickLinkViewSet,
    VanBanQuyCheViewSet,
)

router = DefaultRouter()
router.register(r'baiviet',   BaiVietViewSet)
router.register(r'slider',    SliderViewSet)
router.register(r'quicklink', QuickLinkViewSet)
router.register(r'van-ban',   VanBanQuyCheViewSet)   # ✅ Thêm vào cùng router

urlpatterns = [
    path('', include(router.urls)),
]