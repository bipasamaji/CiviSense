from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DrainageZoneViewSet, RainfallRecordViewSet, FloodRiskViewSet, predict_flood_risk
)

router = DefaultRouter()
router.register('zones', DrainageZoneViewSet)
router.register('rainfall', RainfallRecordViewSet)
router.register('floodrisk', FloodRiskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predict/', predict_flood_risk),
]
