# Generated by Django 4.1 on 2022-09-27 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0004_suscripcion_dnisuscripciones1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suscripcion',
            name='dniSuscripciones1',
        ),
        migrations.AddField(
            model_name='suscripcion',
            name='contraSuscripcion',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]