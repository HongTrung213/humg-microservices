from rest_framework import viewsets
from .models import DotThi, LichSuThi, BaoLuuDiem
from .serializers import DotThiSerializer, LichSuThiSerializer, BaoLuuDiemSerializer

class DotThiViewSet(viewsets.ModelViewSet):
    queryset = DotThi.objects.all()
    serializer_class = DotThiSerializer

class LichSuThiViewSet(viewsets.ModelViewSet):
    queryset = LichSuThi.objects.all()
    serializer_class = LichSuThiSerializer

class BaoLuuDiemViewSet(viewsets.ModelViewSet):
    queryset = BaoLuuDiem.objects.all()
    serializer_class = BaoLuuDiemSerializer