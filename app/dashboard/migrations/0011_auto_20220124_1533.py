# Generated by Django 3.1.6 on 2022-01-24 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20220124_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Current price'),
        ),
        migrations.AlterField(
            model_name='holding',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 24, 15, 33, 0, 564871)),
        ),
        migrations.AlterField(
            model_name='holding',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 24, 15, 33, 0, 564907)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Quantity'),
        ),
    ]
