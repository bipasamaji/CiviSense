from rest_framework import viewsets
from .models import WaterZone, WaterSupplyRecord
from .serializers import WaterZoneSerializer, WaterSupplyRecordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from ml_models.water import check_water_anomaly

class WaterAnomalyCheckView(APIView):
    def post(self, request):
        supply_hours = request.data.get("supply_hours")
        pressure = request.data.get("pressure")
        if None in [supply_hours, pressure]:
            return Response({"error": "All features required"}, status=400)
        is_anomaly = check_water_anomaly(supply_hours, pressure)
        return Response({"anomaly": is_anomaly})

class WaterZoneViewSet(viewsets.ModelViewSet):
    queryset = WaterZone.objects.all()
    serializer_class = WaterZoneSerializer
    permission_classes = [IsAuthenticated]

class WaterSupplyRecordViewSet(viewsets.ModelViewSet):
    queryset = WaterSupplyRecord.objects.all()
    serializer_class = WaterSupplyRecordSerializer
    permission_classes = [IsAuthenticated]

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def detect_water_anomaly(request):
#     supply_hours = request.data.get('supply_hours')
#     avg_pressure = request.data.get('avg_pressure')
#     # Dummy anomaly detection
#     anomaly = float(supply_hours) < 2 or float(avg_pressure) < 1.0
#     return Response({"anomaly": anomaly})
