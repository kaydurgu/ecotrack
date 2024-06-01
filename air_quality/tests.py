from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Sensor
from .serializers import SensorSerializer

class SensorUpdateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sensor = Sensor.objects.create(name='Test Sensor', type='Type A', model='Model 123', location='Location 1')

    def test_update_sensor(self):
        updated_data = {
            'name': 'Updated Sensor',
            'type': 'Type B',
            'model': 'Model XYZ',
            'location': 'Location 2'
        }
        url = reverse('sensor-update', kwargs={'pk': self.sensor.pk})
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sensor.refresh_from_db()
        self.assertEqual(self.sensor.name, updated_data['name'])
        self.assertEqual(self.sensor.type, updated_data['type'])
        self.assertEqual(self.sensor.model, updated_data['model'])
        self.assertEqual(self.sensor.location, updated_data['location'])
class SensorDeleteViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sensor = Sensor.objects.create(name='Test Sensor', type='Type A', model='Model 123', location='Location 1')

    def test_delete_sensor(self):
        initial_count = Sensor.objects.count()
        url = reverse('sensor-delete', kwargs={'pk': self.sensor.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sensor.objects.count(), initial_count - 1)