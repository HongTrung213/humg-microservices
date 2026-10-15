from rest_framework import serializers
from .models import DanhMuc, BaiViet, Slider, QuickLink, VanBanQuyChe


class DanhMucSerializer(serializers.ModelSerializer):
    so_bai_viet = serializers.SerializerMethodField()

    class Meta:
        model = DanhMuc
        fields = '__all__'

    def get_so_bai_viet(self, obj):
        return obj.cac_bai_viet.count()


class BaiVietSerializer(serializers.ModelSerializer):
    category = DanhMucSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=DanhMuc.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = BaiViet
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class QuickLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickLink
        fields = '__all__'


class VanBanQuyCheSerializer(serializers.ModelSerializer):
    class Meta:
        model = VanBanQuyChe
        fields = '__all__'