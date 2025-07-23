from rest_framework import serializers
from .models import TrafficZone, TrafficRecord

class TrafficZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficZone
        fields = '__all__'

class TrafficRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficRecord
        fields = '__all__'
