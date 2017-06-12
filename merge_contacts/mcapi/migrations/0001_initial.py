# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(default=0)),
                ('email_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='phone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcapi.User'),
        ),
        migrations.AddField(
            model_name='emails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcapi.User'),
        ),
    ]
