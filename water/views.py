from rest_framework import viewsets
from .models import WaterZone, WaterSupplyRecord
from .serializers import WaterZoneSerializer, WaterSupplyRecordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class WaterZoneViewSet(viewsets.ModelViewSet):
    queryset = WaterZone.objects.all()
    serializer_class = WaterZoneSerializer
    permission_classes = [IsAuthenticated]

class WaterSupplyRecordViewSet(viewsets.ModelViewSet):
    queryset = WaterSupplyRecord.objects.all()
    serializer_class = WaterSupplyRecordSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def detect_water_anomaly(request):
    supply_hours = request.data.get('supply_hours')
    avg_pressure = request.data.get('avg_pressure')
    # Dummy anomaly detection
    anomaly = float(supply_hours) < 2 or float(avg_pressure) < 1.0
    return Response({"anomaly": anomaly})
