from rest_framework import viewsets
from .models import Khoa, NganhDaoTao, SinhVien
from .serializers import KhoaSerializer, NganhDaoTaoSerializer, SinhVienSerializer

class KhoaViewSet(viewsets.ModelViewSet):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer

class NganhDaoTaoViewSet(viewsets.ModelViewSet):
    queryset = NganhDaoTao.objects.all()
    serializer_class = NganhDaoTaoSerializer

class SinhVienViewSet(viewsets.ModelViewSet):
    queryset = SinhVien.objects.all()
    serializer_class = SinhVienSerializer