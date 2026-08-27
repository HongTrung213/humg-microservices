from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThongBaoViewSet, CanhBaoViewSet

router = DefaultRouter()
router.register(r'thongbao', ThongBaoViewSet)
router.register(r'canhbao', CanhBaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
