# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateField(blank=True, null=True),
        ),
    ]