# Coinbase Auth imports
import hashlib
import hmac
import time
from datetime import datetime

from django.db import models
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from djmoney.models.fields import MoneyField
from requests.auth import AuthBase

from accounts.models import CustomUser

TYPES = [
    ("crypto", "Crypto currency"),
    ("stock", "Stock asset")
]


class Account(models.Model):
    """
        Account Class to display actual total
        balance for a user
    """

    id = models.AutoField(
        primary_key=True,
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=True,
    )
    created = models.DateTimeField(
        blank=True,
    )
    updated = models.DateTimeField(
        blank=True,
    )

    @property
    def balance(self):
        myholdings = [
            holding.value for holding in Holding.objects.filter(
            user=self.user,
        )
        ]
        return sum(myholdings)

    class Meta:
        verbose_name = "Account"

    def __str__(self):
        return f"Account_{self.user}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def update_holding(self):
        # TODO : This function to update actual user holdings
        pass


class Currency(models.Model):
    id = models.CharField(
        max_length=5,
        primary_key=True,
    )
    crypto = models.BooleanField(
        default=True,
    )
    price = models.FloatField(
        verbose_name="Current price",
    )
    name = models.CharField(
        max_length=20,
        blank=False
    )
    created = models.DateTimeField(
        blank=True,
    )
    updated = models.DateTimeField(
        blank=True,
    )
    type = models.CharField(
        max_length=25,
        choices=TYPES
    )

    def update_price(self):
        # TODO : update auto price
        pass

    def __str__(self):
        return f"{self.name}"


class Holding(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    created = models.DateTimeField(
        default=datetime.now(),
        blank=True,
    )
    updated = models.DateTimeField(
        default=datetime.now(),
        blank=True,
    )

    @property
    def quantity(self):
        quantity = Transaction.objects.filter(
            user=self.user,
            currency=self.currency
        ).aggregate(
            Sum(
                "quantity"
            )
        ).get(
            "quantity__sum"
        )
        return quantity

    @property
    def value(self):
        quantity = self.quantity
        price = self.currency.price
        value = quantity * price
        return value

    def __str__(self):
        return f"{self.user.name} {self.currency.type}"

    def add_transaction(self):
        # TODO : Add new transaction to update holding
        pass


class Transaction(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    date = models.DateField(
        default=datetime.now,
        blank=False,
        null=False,
    )
    quantity = models.FloatField(
        verbose_name="Quantity",
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    price = models.DecimalField(
        verbose_name="Price",
        max_digits=6,
        decimal_places=2
    )
    type = models.CharField(
        max_length=25,
        choices=TYPES
    )

    def save(self, *args, **kwargs):
        holding = Holding.objects.get_or_create(
            user=self.user,
            currency=self.currency,
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"

# class Balance(models.Model):
#     pass
# class Portfolio(models.Model):
#     CRYPTO = "crypto"
#     TYPES = [
#         (CRYPTO, "Currency"),
#     ]
#
#     portfolio_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
#     account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True, null=True)
#     type = models.CharField(max_length=25, blank=True, choices=TYPES, unique=True)
#     total = MoneyField(
#         decimal_places=2,
#         default=0,
#         default_currency='USD',
#         max_digits=11,
#     )
#     last_update = models.DateField(blank=True, null=True, default=datetime.now)
#
#     def __str__(self):
#         return f"Portfolio_{self.name} de {self.user}"
#
#     def save(self, *args, **kwargs):
#         transactions = Transaction.objects.filter(user=self.user)
#         totalTransactions = 0
#         for transaction in transactions:
#             totalTransactions = totalTransactions + (transaction.quantity * transaction.crypto.price)
#         self.total = totalTransactions
#         self.account = Account.objects.filter(user=self.user).first()
#         super().save(*args, **kwargs)
