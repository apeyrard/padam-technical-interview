# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_date',
            field=models.DateTimeField(verbose_name='Date de réservation'),
        ),
    ]
