# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-25 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20180125_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
