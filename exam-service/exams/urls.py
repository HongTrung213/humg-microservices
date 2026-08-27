from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DotThiViewSet, LichSuThiViewSet, BaoLuuDiemViewSet

router = DefaultRouter()
router.register(r'dotthi', DotThiViewSet)
router.register(r'lichsuthi', LichSuThiViewSet)
router.register(r'baoluudiem', BaoLuuDiemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
