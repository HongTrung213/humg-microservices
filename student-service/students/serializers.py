from rest_framework import serializers
from .models import Khoa, NganhDaoTao, SinhVien

class KhoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khoa
        fields = '__all__'

class NganhDaoTaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NganhDaoTao
        fields = '__all__'

class SinhVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhVien
        fields = '__all__'
