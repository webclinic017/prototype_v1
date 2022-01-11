from datetime import datetime

from django.db import models
from djmoney.models.fields import MoneyField

from accounts.models import CustomUser


class Holding(models.Model):
    holding_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)


class Crypto(models.Model):
    crypto_id = models.CharField(max_length=5, primary_key=True)
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    name = models.CharField(max_length=20, blank=False)
    last_update = models.DateField(blank=True, null=True)


class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=False, null=False, auto_now=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True)
    # Auto this user
