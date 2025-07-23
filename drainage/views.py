from rest_framework import viewsets
from .models import DrainageZone, RainfallRecord, FloodRisk
from .serializers import DrainageZoneSerializer, RainfallRecordSerializer, FloodRiskSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class DrainageZoneViewSet(viewsets.ModelViewSet):
    queryset = DrainageZone.objects.all()
    serializer_class = DrainageZoneSerializer
    permission_classes = [IsAuthenticated]

class RainfallRecordViewSet(viewsets.ModelViewSet):
    queryset = RainfallRecord.objects.all()
    serializer_class = RainfallRecordSerializer
    permission_classes = [IsAuthenticated]

class FloodRiskViewSet(viewsets.ModelViewSet):
    queryset = FloodRisk.objects.all()
    serializer_class = FloodRiskSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predict_flood_risk(request):
    zone_id = request.data.get('zone_id')
    rainfall = request.data.get('rainfall')
    # Dummy risk prediction
    risk = "High" if rainfall and float(rainfall) > 60 else "Low"
    return Response({"zone_id": zone_id, "predicted_risk": risk})
