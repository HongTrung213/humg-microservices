from rest_framework import viewsets
from .models import LopBoiDuong, DangKyLop
from .serializers import LopBoiDuongSerializer, DangKyLopSerializer

class LopBoiDuongViewSet(viewsets.ModelViewSet):
    queryset = LopBoiDuong.objects.all()
    serializer_class = LopBoiDuongSerializer

class DangKyLopViewSet(viewsets.ModelViewSet):
    queryset = DangKyLop.objects.all()
    serializer_class = DangKyLopSerializer