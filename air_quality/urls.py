from django.urls import path
from .views import SensorListView, SensorDetailView

urlpatterns = [
    path('list/', SensorListView.as_view(), name='sensor-list'),
    path('<int:pk>', SensorDetailView.as_view(), name='sensor-list')
]