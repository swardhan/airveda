from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import DeviceSerializer
from .models import Device, TemperatureReading, HumidityReading

# Device CRUD API
class DeviceViewSet(viewsets.ModelViewSet):
	queryset = Device.objects.all().order_by('name')
	serializer_class = DeviceSerializer

# API to return readings
class DeviceCustomView(APIView):

	def get(self, request, uid, parameter, format=None):
		start_on = request.GET.get('start_on').replace('T', ' ')
		end_on = request.GET.get('end_on').replace('T', ' ')
		
		# Find Device exception Handling
		try:
			device = Device.objects.get(uid=uid)
		except:
			return Response({'message':'device not found'})

		if parameter == 'temperature':
			result = TemperatureReading.objects.filter(device_id=uid).filter(created__range=[start_on, end_on]).values()

		elif parameter == 'humidity':
			result = HumidityReading.objects.filter(uid=uid).filter(created__range=[start_on, end_on]).values()
			
		else:
			return Response({'message':'wrong parameter'})

		data = {
			'uid': uid,
			'result': list(result)
		}

		return Response(data, status=status.HTTP_200_OK)