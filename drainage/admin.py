from django.contrib import admin
from .models import DrainageZone, RainfallRecord, FloodRisk

admin.site.register(DrainageZone)
admin.site.register(RainfallRecord)
admin.site.register(FloodRisk)
# Register your models here.
