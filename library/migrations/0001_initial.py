# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 20:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='borrowingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_checked_out', models.DateField()),
                ('date_returned', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=288, null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_id', models.IntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.MinLengthValidator(5)])),
                ('description', models.CharField(max_length=144)),
                ('parts', models.CharField(max_length=144)),
                ('brand', models.CharField(max_length=144)),
                ('model', models.CharField(max_length=144)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_created', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('zip', models.CharField(max_length=5)),
                ('late_tools', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Tool'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.User'),
        ),
        migrations.AddField(
            model_name='borrowinghistory',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Tool'),
        ),
        migrations.AddField(
            model_name='borrowinghistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.User'),
        ),
    ]
