from rest_framework import viewsets
from .models import TrafficZone, TrafficRecord
from .serializers import TrafficZoneSerializer, TrafficRecordSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# CRUD
class TrafficZoneViewSet(viewsets.ModelViewSet):
    queryset = TrafficZone.objects.all()
    serializer_class = TrafficZoneSerializer
    permission_classes = [IsAuthenticated]

class TrafficRecordViewSet(viewsets.ModelViewSet):
    queryset = TrafficRecord.objects.all()
    serializer_class = TrafficRecordSerializer
    permission_classes = [IsAuthenticated]

# ML Prediction Endpoint (Dummy)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predict_traffic(request):
    # Replace with real model inference!
    zone_id = request.data.get('zone_id')
    timestamp = request.data.get('timestamp')
    # For demo, just return a fake congestion level
    return Response({"zone_id": zone_id, "timestamp": timestamp, "predicted_congestion": 7})
