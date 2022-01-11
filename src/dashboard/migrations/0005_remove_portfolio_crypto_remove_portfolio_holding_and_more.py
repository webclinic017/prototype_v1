# Generated by Django 4.0 on 2022-01-10 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_crypto_price_currency_alter_crypto_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='crypto',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='holding',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='value',
        ),
        migrations.AddField(
            model_name='transaction',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.portfolio'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
