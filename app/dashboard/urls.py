from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import DashboardHomeList, DashboardAddCrypto, TransactionCreate, TransactionUpdate, TransactionDelete, \
    TransactionDetail, TransactionsList, WalletsList, HoldingsList, CurrenciesList

urlpatterns = [
    path('', login_required(DashboardHomeList.as_view(), login_url='home'), name="dashboard-home"),
    path('add/', login_required(DashboardAddCrypto.as_view(), login_url='home'), name="dashboard-add"),

    path('transaction/add', login_required(TransactionCreate.as_view(), login_url='home'),
         name="add-transaction"),
    path('transaction/<int:pk>/edit', login_required(TransactionUpdate.as_view(), login_url='home'),
         name="edit-transaction"),
    path('transaction/<int:pk>/delete', login_required(TransactionDelete.as_view(), login_url='home'),
         name="delete-transaction"),
    path('transaction/<int:pk>/detail', login_required(TransactionDetail.as_view(), login_url='home'),
         name="detail-transaction"),

    path('transactions', login_required(TransactionsList.as_view(), login_url='home'), name="list-transactions"),

    path('wallets', login_required(WalletsList.as_view(), login_url='home'), name="list-wallets"),

    path('assets', login_required(HoldingsList.as_view(), login_url='home'), name="list-assets"),

    path('currencies', login_required(CurrenciesList.as_view(), login_url='home'), name="list-currencies"),

    # path('add-bank/', login_required(BrokerApiCreate.as_view(), login_url='home'), name="dashboard-add-bank"),
]
