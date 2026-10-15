from rest_framework import serializers
from .models import Khoa, NganhDaoTao, SinhVien


class KhoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Khoa
        fields = '__all__'


class NganhDaoTaoSerializer(serializers.ModelSerializer):
    khoa = KhoaSerializer(read_only=True)

    class Meta:
        model = NganhDaoTao
        fields = '__all__'


class SinhVienSerializer(serializers.ModelSerializer):
    # Nested objects cho portal
    khoa_info = KhoaSerializer(source='khoa', read_only=True)
    nganh_info = NganhDaoTaoSerializer(source='nganh', read_only=True)

    class Meta:
        model = SinhVien
        fields = '__all__'