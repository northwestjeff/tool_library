# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-31 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20180125_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='date_out',
            field=models.DateField(blank=True, null=True),
        ),
    ]
