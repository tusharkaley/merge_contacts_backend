# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mcapi', '0003_auto_20170611_0342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='email_id',
        ),
        migrations.AddField(
            model_name='contacts',
            name='company',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contacts',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contacts',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='emails',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcapi.Contacts'),
        ),
        migrations.AlterField(
            model_name='emails',
            name='email_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phones',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mcapi.Contacts'),
        ),
        migrations.AlterField(
            model_name='phones',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=50),
        ),
    ]