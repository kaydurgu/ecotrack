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
