from django.contrib import admin
from .models import *

admin.site.register(Device)
admin.site.register(TemperatureReading)
admin.site.register(HumidityReading)
