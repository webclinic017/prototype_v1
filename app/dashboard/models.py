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


class Type(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    name = models.CharField(
        max_length=25,
        unique=True,
    )

    def __str__(self):
        return f"{self.name}"


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
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
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
    type = models.OneToOneField(
        Type,
        on_delete=models.CASCADE,
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
        if not quantity:
            quantity = 0
        return quantity

    @property
    def value(self):
        quantity = self.quantity
        price = self.currency.price
        value = quantity * price
        return value

    @property
    def average_purchase_price(self):
        purchases_prices = [
            transaction.purchase_price for transaction in Transaction.objects.filter(
                user=self.user,
                currency=self.currency
            )
        ]
        average_purchase_price = sum(purchases_prices) / self.quantity
        return average_purchase_price

    @property
    def gain_loss_holding(self):
        percent = (self.currency.price - self.average_purchase_price) / self.average_purchase_price
        percent = round(percent, 2)
        if percent > 0:
            sign = '+'
        elif percent < 0:
            sign = '-'
        else:
            sign = ' '
        return sign + str(percent) + '%'

    def __str__(self):
        return f"{self.user.name} {self.currency.type}"

    def add_transaction(self):
        # TODO : Add new transaction to update holding
        pass


class Portfolio(models.Model):
    id = models.AutoField(
        primary_key=True,
    )
    type = models.OneToOneField(
        Type,
        on_delete=models.CASCADE,
        unique=True
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    @property
    def value(self):
        mywallets = [
            holding.value for holding in Holding.objects.filter(
                user=self.user,
                type=self.type,
            )
        ]
        if not mywallets:
            mywallets = 0
        return mywallets[0]


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
    price = models.FloatField(
        verbose_name="Price",
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
    )

    @property
    def purchase_price(self):
        quantity = self.quantity
        price = self.price
        purchase_price = quantity * price
        return purchase_price

    def save(self, *args, **kwargs):
        holding = Holding.objects.get_or_create(
            user=self.user,
            currency=self.currency,
            type=self.type,
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"
