from rest_framework import serializers
from .models import DotThi, LichSuThi, BaoLuuDiem

class DotThiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DotThi
        fields = '__all__'

class LichSuThiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LichSuThi
        fields = '__all__'

class BaoLuuDiemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaoLuuDiem
        fields = '__all__'
