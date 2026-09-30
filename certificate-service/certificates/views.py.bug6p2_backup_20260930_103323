from rest_framework import viewsets
from .models import DanhMucChungChi, ChungChi
from .serializers import DanhMucChungChiSerializer, ChungChiSerializer

class DanhMucChungChiViewSet(viewsets.ModelViewSet):
    queryset = DanhMucChungChi.objects.all()
    serializer_class = DanhMucChungChiSerializer

class ChungChiViewSet(viewsets.ModelViewSet):
    queryset = ChungChi.objects.all()
    serializer_class = ChungChiSerializer
