# Create your views here.
from datetime import date

import finnhub
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView

from dashboard.forms import UpdateTransactionForm
from dashboard.models import Account, Transaction, Holding, Portfolio, Currency

"""
--------------- DASHBOARD ---------------
"""


class DashboardHomeList(ListView):
    model = Account
    template_name = "dashboard/dashboard.html"
    context_object_name = "accounts"

    def get_queryset(self):
        return Account.objects.filter(
            user=self.request.user
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['holdings'] = Holding.objects.filter(
            user=self.request.user
        )
        context['transactions'] = Transaction.objects.filter(
            user=self.request.user
        )
        context['wallets'] = Portfolio.objects.filter(
            user=self.request.user
        )
        return context


class DashboardAddCrypto(CreateView):
    model = Account
    template_name = "dashboard/portfolio_create.html"
    fields = ['name', 'type']
    success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


"""
--------------- TRANSACTIONS -------------
"""


class TransactionCreate(CreateView):
    model = Transaction
    template_name = "transaction/create_transaction.html"
    fields = (
        "date",
        "quantity",
        "currency",
        "price",
    )
    success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        form.instance.type = form.instance.currency.type
        today = date.today()
        portfolio = Portfolio.objects.filter(
            user=self.request.user,
            type=form.instance.type,
        )
        if not portfolio:
            Portfolio.objects.create(
                user=self.request.user,
                type=form.instance.type,
            )
        return super().form_valid(form)


class TransactionUpdate(UpdateView):
    model = Transaction
    form_class = UpdateTransactionForm
    template_name = "transaction/update_transaction.html"
    success_url = reverse_lazy("dashboard-home")


class TransactionDelete(DeleteView):
    model = Transaction
    template_name = "transaction/delete_transaction.html"
    success_url = reverse_lazy("dashboard-home")


class TransactionDetail(DetailView):
    model = Transaction
    template_name = "transaction/detail_transaction.html"


class TransactionsList(ListView):
    model = Transaction
    template_name = "transaction/list_transactions.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.filter(
            user=self.request.user
        )


"""
--------------- WALLETS ---------------
"""


class WalletsList(ListView):
    model = Portfolio
    template_name = "wallet/list_wallets.html"
    context_object_name = "wallets"

    def get_queryset(self):
        return Portfolio.objects.filter(
            user=self.request.user
        )


"""
--------------- ASSETS ---------------
"""


class HoldingsList(ListView):
    model = Holding
    template_name = "asset/list_assets.html"
    context_object_name = "assets"

    def get_queryset(self):
        return Holding.objects.filter(
            user=self.request.user
        )


"""
--------------- CURRENCIES ------------
"""


class CurrenciesList(ListView):
    model = Currency
    template_name = "currency/list_currencies.html"
    context_object_name = "currencies"
