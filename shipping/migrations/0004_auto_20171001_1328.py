# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0003_auto_20171001_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]