from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from dashboard.models import Portfolio, Account


def add(request):
    requestContent = request.GET
    code = requestContent.__getitem__("code")
    connection_id = requestContent.__getitem__("connection_id")
    return HttpResponse(connection_id)



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
