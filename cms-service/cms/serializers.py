from rest_framework import serializers
from .models import BaiViet, Slider, QuickLink

class BaiVietSerializer(serializers.ModelSerializer):
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