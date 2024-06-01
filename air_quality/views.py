from django.shortcuts import render
from rest_framework import permissions, viewsets, generics
from .models import Sensor, Alert, Data
from .serializers import SensorSerializer, DataSerializer, AlertSerializer

# Create your views here.

class IsInGroup(permissions.BasePermission):
    group_name = None
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            return request.user.groups.filter(name=self.group_name).exists()
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()
class IsAdminUser(IsInGroup):
    group_name = 'Admin'
class IsWorkerUser(IsInGroup):
    group_name = 'Worker'

class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAdminOrReadOnly]
class SensorCreateView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAdminUser]
class ActiveSensorListView(generics.ListAPIView):
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Sensor.objects.filter(status='active')
class InactiveSensorListView(generics.ListAPIView):
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Sensor.objects.filter(status='inactive')
class MaintenanceSensorListView(generics.ListAPIView):
    serializer_class = SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Sensor.objects.filter(status='maintenance')

class AlertListView(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAdminOrReadOnly]

class LowSeverityAlertListView(generics.ListAPIView):
    queryset = Alert.objects.filter(severity='low')
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

class MediumSeverityAlertListView(generics.ListAPIView):
    queryset = Alert.objects.filter(severity='medium')
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

class HighSeverityAlertListView(generics.ListAPIView):
    queryset = Alert.objects.filter(severity='high')
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

class OkSeverityAlertListView(generics.ListAPIView):
    queryset = Alert.objects.filter(severity='ok')
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlertDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlertUpdateView(generics.UpdateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [permissions.IsAuthenticated ]

class AlertDeleteView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAdminOrReadOnly]


class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAdminOrReadOnly]

class SensorDeleteView(generics.DestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAdminOrReadOnly]

class DataListView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [permissions.IsAuthenticated]

class DataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAdminOrReadOnly]

class DataCreateView(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAdminOrReadOnly]

class DataUpdateView(generics.UpdateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAdminOrReadOnly]

class DataDeleteView(generics.DestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAdminOrReadOnly]