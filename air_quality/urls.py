from django.urls import path
from .views import (SensorListView, SensorDetailView, SensorCreateView, ActiveSensorListView,InactiveSensorListView,
        MaintenanceSensorListView)
import views
urlpatterns = [
    path('list/', SensorListView.as_view(), name='sensor-list'),
    path('<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('crupdlt/', SensorCreateView.as_view(), name='sensor-create'),
    path('list_of_active_sensors/', ActiveSensorListView.as_view(), name='active-sensor-list'),
    path('list_of_inactive_sensors/', InactiveSensorListView.as_view(), name='inactive-sensor-list'),
    path('list_of_maintenance_sensors/', MaintenanceSensorListView.as_view(), name='maintenance-sensor-list'),
    path('list_of_alerts/', views.AlertListView.as_view(), name='alert-list'),
    path('list_low_danger/', views.LowSeverityAlertListView.as_view(), name='low-severity-alert-list'),
    path('list_medium_danger/', views.MediumSeverityAlertListView.as_view(), name='medium-severity-alert-list'),
    path('list_high_danger/', views.HighSeverityAlertListView.as_view(), name='high-severity-alert-list'),
    path('list_no_danger/', views.OkSeverityAlertListView.as_view(), name='ok-severity-alert-list'),

]