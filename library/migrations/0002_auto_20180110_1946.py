# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-10 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='borrower',
            field=models.CharField(default=True, max_length=233, null=True),
        ),
    ]
