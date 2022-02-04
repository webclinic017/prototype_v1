from django.contrib import admin

# Register your models here.
from accounts.models import CustomUser
from .models import Currency, Transaction, Account, Holding, Portfolio, Type


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "created",
        "updated",
        "balance",
    )


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "crypto",
        "price",
        "name",
        "created",
        "updated",
        "type",
        "updated_price",
    )


@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "currency",
        "user",
        "created",
        "updated",
        "quantity",
        "value",
        "average_purchase_price",
        "gain_loss_holding"
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "quantity",
        "user",
        "currency",
        "price",
        "purchase_price",
    )


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "email",
        "is_admin",
        "is_staff",
    )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
        "user",
        "value",
    )
