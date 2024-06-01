from django.contrib import admin

from .models import Sensor, Data, Alert

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'model', 'location', 'status', 'installation_date')
    search_fields = ('name', 'type', 'model', 'location', 'status')
    list_filter = ('type', 'status', 'installation_date')

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'pm25', 'pm10', 'co2', 'temperature', 'humidity', 'timestamp')
    search_fields = ('sensor__name', 'timestamp')
    list_filter = ('timestamp',)

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'description','last_timecheckedby', 'warning_notes')
    search_fields = ('sensor__name', 'description', 'timestamp')
    list_filter = ('last_timestamp',)