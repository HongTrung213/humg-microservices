from rest_framework import serializers
from .models import DotThi, LichSuThi, BaoLuuDiem

class DotThiSerializer(serializers.ModelSerializer):
    mon_thi = serializers.CharField(read_only=True)
    loai_display = serializers.CharField(source='get_loai_display', read_only=True)
    so_thi_sinh = serializers.SerializerMethodField()

    class Meta:
        model = DotThi
        fields = '__all__'

    def get_so_thi_sinh(self, obj):
        return obj.lich_su_thi.count()

class LichSuThiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LichSuThi
        fields = '__all__'

class BaoLuuDiemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaoLuuDiem
        fields = '__all__'
