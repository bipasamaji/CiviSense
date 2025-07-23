from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaterZoneViewSet, WaterSupplyRecordViewSet, WaterAnomalyCheckView

router = DefaultRouter()
router.register('zones', WaterZoneViewSet)
router.register('records', WaterSupplyRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detect/', WaterAnomalyCheckView.as_view(), name='water_anomaly_check'),
]
