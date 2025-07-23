from rest_framework import serializers
from .models import WaterZone, WaterSupplyRecord

class WaterZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterZone
        fields = '__all__'

class WaterSupplyRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSupplyRecord
        fields = '__all__'
