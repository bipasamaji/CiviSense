from django.db import models

class DrainageZone(models.Model):
    name = models.CharField(max_length=100)
    elevation = models.FloatField()
    drainage_capacity = models.FloatField()
    geojson = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name

class RainfallRecord(models.Model):
    zone = models.ForeignKey(DrainageZone, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    rainfall_mm = models.FloatField()

class FloodRisk(models.Model):
    zone = models.ForeignKey(DrainageZone, on_delete=models.CASCADE)
    date = models.DateField()
    risk_level = models.CharField(max_length=10, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])