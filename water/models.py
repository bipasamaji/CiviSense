from django.db import models

class WaterZone(models.Model):
    name = models.CharField(max_length=100)
    geojson = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class WaterSupplyRecord(models.Model):
    zone = models.ForeignKey(WaterZone, on_delete=models.CASCADE)
    date = models.DateField()
    supply_hours = models.FloatField()
    avg_pressure = models.FloatField()
    anomaly_flag = models.BooleanField(default=False)