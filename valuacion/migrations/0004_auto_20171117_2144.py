# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-18 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valuacion', '0003_auto_20171117_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuacion',
            name='val_2015',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2016',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_okm',
            field=models.IntegerField(null=True),
        ),
    ]