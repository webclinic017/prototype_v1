from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import DashboardHomeList, DashboardAddCrypto

urlpatterns = [
    path('', login_required(DashboardHomeList.as_view(), login_url='login'), name="dashboard-home"),
    path('add/', login_required(DashboardAddCrypto.as_view(), login_url='login'), name="dashboard-add"),
]