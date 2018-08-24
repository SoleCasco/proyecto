# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-16 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valuacion', '0005_auto_20171117_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2009',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2010',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2011',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2012',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2013',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2014',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2015',
        ),
        migrations.RemoveField(
            model_name='valuacion',
            name='val_2016',
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='valuacion',
            name='val_8',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='cod_fabrica',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='cod_marca',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='cod_modelo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='cod_tipo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='marca',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='origen',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='tipo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='tv',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1993',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1994',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1995',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1996',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1997',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1998',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_1999',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2000',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2001',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2002',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2003',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2004',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2005',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2006',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2007',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_2008',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='valuacion',
            name='val_okm',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]