# Generated by Django 2.2.8 on 2022-01-05 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0019_auto_20211203_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webservicedevice',
            name='web_service_handler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyscada.DeviceHandler'),
        ),
    ]