from django.db import models
from django.conf import settings

class Feedback(models.Model):
    FEEDBACK_TYPES = [
        ('traffic', 'Traffic Jam'),
        ('water', 'Water Shortage'),
        ('drainage', 'Drain Overflow')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=FEEDBACK_TYPES)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)