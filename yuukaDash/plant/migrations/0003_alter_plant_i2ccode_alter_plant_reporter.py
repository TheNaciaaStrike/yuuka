# Generated by Django 4.2.13 on 2024-05-20 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_reporterdevice_ip_address_and_more'),
        ('plant', '0002_plant_i2ccode_plant_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='I2CCode',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.reporterdevice'),
        ),
    ]