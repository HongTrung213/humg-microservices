from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DanhMucChungChiViewSet, ChungChiViewSet

router = DefaultRouter()
router.register(r'danhmuc', DanhMucChungChiViewSet)
router.register(r'chungchi', ChungChiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]