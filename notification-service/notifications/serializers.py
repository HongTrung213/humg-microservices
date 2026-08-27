from rest_framework import serializers
from .models import ThongBao, CanhBao

class ThongBaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThongBao
        fields = '__all__'

class CanhBaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CanhBao
        fields = '__all__'
