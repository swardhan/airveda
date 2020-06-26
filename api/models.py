from django.db import models
from django.utils import timezone

class Device(models.Model):
	name = models.CharField(max_length=200)
	uid = models.CharField(max_length=50, primary_key=True)

	def __str__(self):
		return "Name: " + self.name + ", UID: "+self.uid

class TemperatureReading(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	reading = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Device:%s, Temp. Reading: %s, Time: %s" % (self.device.uid, self.reading, self.created)

class HumidityReading(models.Model):
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	reading = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Device:%s, Humidity Reading: %s, Time: %s" % (self.device.uid, self.reading, self.created)