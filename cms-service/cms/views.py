from rest_framework import viewsets
from .models import DanhMuc, BaiViet, Slider, QuickLink, VanBanQuyChe
from .serializers import (
    DanhMucSerializer, BaiVietSerializer, SliderSerializer,
    QuickLinkSerializer, VanBanQuyCheSerializer,
)


class DanhMucViewSet(viewsets.ModelViewSet):
    # ✅ BẮT BUỘC cho DRF router tạo basename
    queryset = DanhMuc.objects.all()
    serializer_class = DanhMucSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.request.query_params.get('slug')
        if slug:
            qs = qs.filter(slug=slug)
        active = self.request.query_params.get('is_active')
        if active is not None:
            qs = qs.filter(is_active=(active.lower() == 'true'))
        return qs


class BaiVietViewSet(viewsets.ModelViewSet):
    # ✅ BẮT BUỘC
    queryset = BaiViet.objects.select_related('category').all()
    serializer_class = BaiVietSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.request.query_params.get('slug')
        if slug:
            qs = qs.filter(slug=slug)
        category_id = self.request.query_params.get('category')
        if category_id:
            qs = qs.filter(category_id=category_id)
        category_slug = self.request.query_params.get('category__slug')
        if category_slug:
            qs = qs.filter(category__slug=category_slug)
        return qs


class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class QuickLinkViewSet(viewsets.ModelViewSet):
    queryset = QuickLink.objects.all()
    serializer_class = QuickLinkSerializer


class VanBanQuyCheViewSet(viewsets.ModelViewSet):
    # ✅ BẮT BUỘC
    queryset = VanBanQuyChe.objects.all()
    serializer_class = VanBanQuyCheSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if not (self.request.user and self.request.user.is_authenticated):
            qs = qs.filter(is_active=True)
        slug = self.request.query_params.get('slug')
        if slug:
            qs = qs.filter(slug=slug)
        return qs