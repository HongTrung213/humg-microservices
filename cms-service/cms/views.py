from rest_framework import viewsets
from .models import BaiViet, Slider, QuickLink
from .serializers import BaiVietSerializer, SliderSerializer, QuickLinkSerializer

class BaiVietViewSet(viewsets.ModelViewSet):
    queryset = BaiViet.objects.all()
    serializer_class = BaiVietSerializer

class SliderViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

class QuickLinkViewSet(viewsets.ModelViewSet):
    queryset = QuickLink.objects.all()
    serializer_class = QuickLinkSerializer