import hmac
import time
from datetime import date

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django import forms
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from dashboard.models import Account, Transaction
import requests


class DashboardHomeList(ListView):
    model = Account
    template_name = "dashboard/portfolio_list.html"
    context_object_name = "portfolio"


class DashboardAddCrypto(CreateView):
    model = Account
    template_name = "dashboard/portfolio_create.html"
    fields = ['name', 'type']
    success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


class DashboardAddTransaction(CreateView):
    model = Transaction
    template_name = "dashboard/portfolio_create.html"
    fields = "__all__"
    success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form) 


# class BrokerApiCreate(CreateView):
#     model = BrokerApi
#     success_url = reverse_lazy("dashboard-home")
#     context_object_name = "form"
#     form_class = BrokerApiForm
#
#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.user = self.request.user
#         # url = "https://api.exchange.coinbase.com/transfers"
#         # headers = {
#         #     "Accept": "application/json",
#         #     "cb-access-key": form.instance.api_key,
#         #     "cb-access-passphrase": form.instance.passphrase,
#         #     "cb-access-sign": form.instance.secret_key,
#         #     "cb-access-timestamp": timestamp,
#         # }
#         # response = requests.request("GET", url, headers=headers)
#         response = CoinbaseWalletAuth(form.instance.api_key, form.instance.secret_key)
#         print(vars(form.instance))
#         return super().form_valid(form)


# def add(request):
#     request_content = request.GET
#     code = request_content.__getitem__("code")
#     connection_id = request_content.__getitem__("connection_id")
#
#     data = {"client_id": code, "client_secret": connection_id}
#     url = "https://moneyes-prototypev1-sandbox.biapi.pro/2.0/auth/init"
#     response = requests.post(url, data)
#     return HttpResponse(response)
