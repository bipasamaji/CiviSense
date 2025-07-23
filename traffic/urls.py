from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrafficZoneViewSet, TrafficRecordViewSet, predict_traffic

router = DefaultRouter()
router.register('zones', TrafficZoneViewSet)
router.register('records', TrafficRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('predict/', predict_traffic),
]
