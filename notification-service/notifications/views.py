from rest_framework import viewsets
from .models import ThongBao, CanhBao
from .serializers import ThongBaoSerializer, CanhBaoSerializer

class ThongBaoViewSet(viewsets.ModelViewSet):
    queryset = ThongBao.objects.all()
    serializer_class = ThongBaoSerializer

class CanhBaoViewSet(viewsets.ModelViewSet):
    queryset = CanhBao.objects.all()
    serializer_class = CanhBaoSerializer
