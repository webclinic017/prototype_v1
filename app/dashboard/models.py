# Coinbase Auth imports
import decimal
import math
import time
from datetime import datetime
from decimal import Decimal

import websocket
from django.db import models
from django.db.models import Sum
import finnhub

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
        myBalance = sum(myholdings)
        myBalance = round(myBalance, 2)
        return myBalance

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
        max_length=24,
        primary_key=True,
    )
    crypto = models.BooleanField(
        default=True,
    )
    # ``deprecated -> property updated_price is now the current price
    #price = models.FloatField(
    #    verbose_name="Current price",
    #)
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

    @property
    def updated_price(self):
        finnhub_client = finnhub.Client(api_key="sandbox_c1ksus237fktsl8cmv40")
        quote = finnhub_client.quote(self.id)['c']
        return quote


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
    type = models.ForeignKey(
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
        try:
            quantity = self.quantity
            price = self.currency.updated_price
            value = price * quantity
            value = round(value, 2)
            # TO DO : get precision with price decimals and not only 2
        except ValueError:
            print(ValueError)
            value = 0
        except TypeError:
            print(TypeError)
            value = 0
        except:
            print(f"Error when calculate value {self.currency} Holdings")
            value = 0
        finally:
            return value

    @property
    def average_purchase_price(self):
        try:
            purchases_prices = [
                transaction.purchase_price for transaction in Transaction.objects.filter(
                    user=self.user,
                    currency=self.currency
                )
            ]
            average_purchase_price = sum(purchases_prices) / self.quantity
        except ZeroDivisionError:
            print(ZeroDivisionError)
            average_purchase_price = 0
        except:
            print("Error when calculate Average Purchase Price")
        finally:
            return average_purchase_price

    @property
    def gain_loss_holding(self):
        try:
            percent = ((self.currency.updated_price - self.average_purchase_price) / self.average_purchase_price )* 100
            percent = round(percent, 2)
        except ZeroDivisionError:
            print(ZeroDivisionError)
            percent = 0
        except:
            print(f"Error when calculate gain/loss for {self.id} Holding")
            percent = 0
        finally:
            if percent > 0:
                sign = '+'
            else:
                sign = ' '
            return sign + str(percent) + '%'

    def __str__(self):
        return f"{self.user.name} {self.currency.type}"



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
        wallets = [
            holding.value for holding in Holding.objects.filter(
                user=self.user,
                type=self.type,
            )
        ]
        try:
            mywallets = wallets[0]
        except IndexError:
            print(IndexError)
            mywallets = 0
        except ValueError:
            print(ValueError)
            mywallets = 0
        except:
            print(f"Error to fetch wallets' {self.user}")
            mywallets = 0
        finally:
            return mywallets


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
        verbose_name="Purchase price",
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
