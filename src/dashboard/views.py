from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from dashboard.models import Portfolio, Holding


class DashboardHomeList(ListView):
    model = Holding
    template_name = "dashboard/portfolio_list.html"
    context_object_name = "portfolio"


class DashboardAddCrypto(CreateView):
    model = Portfolio
    template_name = "dashboard/portfolio_create.html"
    fields = ['crypto', 'quantity']
    success_url = reverse_lazy('dashboard-home')
