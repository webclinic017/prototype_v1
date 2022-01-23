# Generated by Django 3.1.6 on 2022-01-22 17:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('crypto', models.BooleanField(default=True)),
                ('price', models.FloatField(verbose_name='Current price')),
                ('name', models.CharField(max_length=20)),
                ('created', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('type', models.CharField(choices=[('crypto', 'Crypto currency'), ('stock', 'Stock asset')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('price', models.FloatField(verbose_name='Price')),
                ('type', models.CharField(choices=[('crypto', 'Crypto currency'), ('stock', 'Stock asset')], max_length=25)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.FloatField(verbose_name='Quantity of None')),
                ('created', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.currency')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(blank=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('balance', models.FloatField(verbose_name='Current balance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
            },
        ),
    ]
