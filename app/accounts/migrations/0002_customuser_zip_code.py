# Generated by Django 4.0 on 2022-01-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
