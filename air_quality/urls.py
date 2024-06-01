from django.urls import path
from .views import (SensorListView, SensorDetailView, SensorCreateView, ActiveSensorListView,InactiveSensorListView,
        MaintenanceSensorListView)
from . import views
urlpatterns = [
    path('list/', SensorListView.as_view(), name='sensor-list'),
    path('<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('<int:pk>/update/', views.SensorUpdateView.as_view(), name='sensor-update'),
    path('<int:pk>/delete/', views.SensorDeleteView.as_view(), name='sensor-delete'),
    path('create/', SensorCreateView.as_view(), name='sensor-create'),

    path('list_of_active_sensors/', ActiveSensorListView.as_view(), name='active-sensor-list'),
    path('list_of_inactive_sensors/', InactiveSensorListView.as_view(), name='inactive-sensor-list'),
    path('list_of_maintenance_sensors/', MaintenanceSensorListView.as_view(), name='maintenance-sensor-list'),


    path('alerts/<int:pk>/', views.AlertDetailView.as_view(), name='alerts-detail'),
    path('alerts/<int:pk>/update/', views.AlertUpdateView.as_view(), name='alert-update'),
    path('alerts/<int:pk>/delete/', views.AlertDeleteView.as_view(), name='alert-delete'),


    path('list_of_alerts/', views.AlertListView.as_view(), name='alert-list'),
    path('list_low_danger/', views.LowSeverityAlertListView.as_view(), name='low-severity-alert-list'),
    path('list_medium_danger/', views.MediumSeverityAlertListView.as_view(), name='medium-severity-alert-list'),
    path('list_high_danger/', views.HighSeverityAlertListView.as_view(), name='high-severity-alert-list'),
    path('list_no_danger/', views.OkSeverityAlertListView.as_view(), name='ok-severity-alert-list'),

    path('data/', views.DataListView.as_view(), name='data-list'),
    path('data/<int:pk>/', views.DataDetailView.as_view(), name='data-detail'),
    path('data/create/', views.DataCreateView.as_view(), name='data-create'),
    path('data/<int:pk>/update/', views.DataUpdateView.as_view(), name='data-update'),
    path('data/<int:pk>/delete/', views.DataDeleteView.as_view(), name='data-delete'),
]