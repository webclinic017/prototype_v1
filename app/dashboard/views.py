import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from dashboard.models import Portfolio, Account


def add(request):
    request_content = request.GET
    code = request_content.__getitem__("code")
    connection_id = request_content.__getitem__("connection_id")

    data = {"client_id": code, "client_secret": connection_id}
    url = "https://moneyes-prototypev1-sandbox.biapi.pro/2.0/auth/init"
    response = requests.post(url, data)
    return HttpResponse(response)


class DashboardHomeList(ListView):
    model = Portfolio
    template_name = "dashboard/portfolio_list.html"
    context_object_name = "portfolio"


class DashboardAddCrypto(CreateView):
    model = Portfolio
    template_name = "dashboard/portfolio_create.html"
    fields = ['name', 'type']
    success_url = reverse_lazy('dashboard-home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)
