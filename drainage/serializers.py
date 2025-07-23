from rest_framework import serializers
from .models import DrainageZone, RainfallRecord, FloodRisk

class DrainageZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrainageZone
        fields = '__all__'

class RainfallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainfallRecord
        fields = '__all__'

class FloodRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloodRisk
        fields = '__all__'
