# Coinbase Auth imports
import hashlib
import hmac
import time
from datetime import datetime

from django.db import models
from djmoney.models.fields import MoneyField
from requests.auth import AuthBase

from accounts.models import CustomUser


class Account(models.Model):
    acc_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=False, null=False, unique=True)

    def __str__(self):
        return f"Account_{self.user.id}"


class Balance(models.Model):
    value = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Balance"

    def __str__(self):
        return str(self.value)

    def save(self, *args, **kwargs):
        pass

        super().save(*args, **kwargs)


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

    def __str__(self):
        return f"{self.name}"


class Portfolio(models.Model):
    CRYPTO = "crypto"
    TYPES = [
        (CRYPTO, "Crypto"),
    ]

    portfolio_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=25, blank=True, choices=TYPES, unique=True)
    total = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )
    last_update = models.DateField(blank=True, null=True, default=datetime.now)

    def __str__(self):
        return f"Portfolio_{self.name} de {self.user}"

    def save(self, *args, **kwargs):
        transactions = Transaction.objects.filter(user=self.user)
        totalTransactions = 0
        for transaction in transactions:
            totalTransactions = totalTransactions + (transaction.quantity * transaction.crypto.price)
        self.total = totalTransactions
        self.account = Account.objects.filter(user=self.user).first()
        super().save(*args, **kwargs)


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=False, null=False, auto_now=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    crypto = models.ForeignKey(Crypto, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True)

    # Auto this user

    def __str__(self):
        return f"{self.transaction_id}"
