# Generated by Django 4.2.13 on 2024-05-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='I2CCode',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='plant',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devices.reporterdevice'),
        ),
    ]
