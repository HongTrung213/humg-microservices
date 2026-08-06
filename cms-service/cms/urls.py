from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BaiVietViewSet, SliderViewSet, QuickLinkViewSet

router = DefaultRouter()
router.register(r'baiviet', BaiVietViewSet)
router.register(r'slider', SliderViewSet)
router.register(r'quicklink', QuickLinkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from .views import VanBanQuyCheViewSet

router = DefaultRouter()
router.register(r'van-ban', VanBanQuyCheViewSet)