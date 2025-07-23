from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaterZoneViewSet, WaterSupplyRecordViewSet, detect_water_anomaly

router = DefaultRouter()
router.register('zones', WaterZoneViewSet)
router.register('records', WaterSupplyRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detect/', detect_water_anomaly),
]
