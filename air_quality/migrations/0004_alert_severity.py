# Generated by Django 5.0.6 on 2024-06-01 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('air_quality', '0003_remove_alert_timestamp_data_pressure_data_wind_speed'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='severity',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low'), ('ok', 'Ok')], default='ok', max_length=10),
        ),
    ]
