from django.contrib import admin

# Register your models here.
from .models import Crypto, Portfolio, Transaction, Account, Balance


@admin.register(Crypto)
class CryptoAdmin(admin.ModelAdmin):
    list_display = (
        "crypto_id",
        "name",
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "user",
    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "acc_id",
        "user",
    )


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = (
        "value",
        "account"
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "transaction_id",
        "date",
        "quantity",
        "crypto",
        "user",
        "portfolio",
    )
