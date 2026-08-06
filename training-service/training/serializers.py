
from rest_framework import serializers
from .models import LopBoiDuong, DangKyLop, LichHoc

class LopBoiDuongSerializer(serializers.ModelSerializer):
    class Meta:
        model = LopBoiDuong
        fields = '__all__'

class DangKyLopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DangKyLop
        fields = '__all__'

class LichHocSerializer(serializers.ModelSerializer):
    class Meta:
        model = LichHoc
        fields = '__all__'
        read_only_fields = ('id',)