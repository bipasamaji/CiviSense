from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DrainageZoneViewSet, RainfallRecordViewSet, FloodRiskViewSet, FloodRiskPredictView
)

router = DefaultRouter()
router.register('zones', DrainageZoneViewSet)
router.register('rainfall', RainfallRecordViewSet)
router.register('floodrisk', FloodRiskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predict/', FloodRiskPredictView.as_view(), name='flood_predict'),
]
