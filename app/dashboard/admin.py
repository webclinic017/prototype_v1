from django.contrib import admin

# Register your models here.
from accounts.models import CustomUser
from .models import Currency, Transaction, Account, Holding


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
