# Generated by Django 3.1.6 on 2022-01-22 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20220122_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holding',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 22, 21, 23, 5, 578271)),
        ),
        migrations.AlterField(
            model_name='holding',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 22, 21, 23, 5, 578305)),
        ),
    ]