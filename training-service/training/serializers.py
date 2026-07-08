from rest_framework import serializers
from .models import LopBoiDuong, DangKyLop

class LopBoiDuongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LopBoiDuong
        fields = '__all__'

class DangKyLopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DangKyLop
        fields = '__all__'