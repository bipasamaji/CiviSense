from django.db import models

class TrafficZone(models.Model):
    name = models.CharField(max_length=100)
    geojson = models.JSONField(null= True, blank= True)

class TrafficRecord(models.Model):
    zone = models.ForeignKey(TrafficZone, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    congestion_level = models.IntegerField()
    avg_speed = models.FloatField(null=True, blank=True)

