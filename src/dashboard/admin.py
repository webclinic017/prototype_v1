from django.contrib import admin

# Register your models here.
from .models import Crypto, Portfolio, Holding, Transaction


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


@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = (
        "holding_id",
        "user",
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