from rest_framework import serializers
from .models import DanhMucChungChi, ChungChi


class DanhMucChungChiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanhMucChungChi
        fields = '__all__'


class ChungChiSerializer(serializers.ModelSerializer):
    # ✅ Trả nested danh_muc (dict) thay vì chỉ id
    danh_muc = DanhMucChungChiSerializer(read_only=True)
    danh_muc_id = serializers.PrimaryKeyRelatedField(
        queryset=DanhMucChungChi.objects.all(),
        source='danh_muc',
        write_only=True,
        required=False,
    )

    class Meta:
        model = ChungChi
        fields = '__all__'