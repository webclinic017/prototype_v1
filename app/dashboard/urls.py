from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import DashboardHomeList, DashboardAddCrypto, DashboardAddTransaction

urlpatterns = [
    path('', login_required(DashboardHomeList.as_view(), login_url='home'), name="dashboard-home"),
    path('add/', login_required(DashboardAddCrypto.as_view(), login_url='home'), name="dashboard-add"),
    path('add-transaction', login_required(DashboardAddTransaction.as_view(), login_url='home'), name="dashboard-add-transaction")
    #path('add-bank/', login_required(BrokerApiCreate.as_view(), login_url='home'), name="dashboard-add-bank"),
]
