# Generated by Django 3.1.6 on 2022-02-01 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_auto_20220201_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holding',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 12, 28, 11, 190298)),
        ),
        migrations.AlterField(
            model_name='holding',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 1, 12, 28, 11, 190427)),
        ),
    ]