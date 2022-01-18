from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from dashboard.models import Portfolio, Account


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