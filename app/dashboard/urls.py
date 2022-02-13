from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import DashboardHomeList, DashboardAddCrypto, TransactionCreate, TransactionUpdate, TransactionDelete, \
    TransactionDetail, TransactionsList, WalletsList, HoldingsList, CurrenciesList

login_url = 'login'

urlpatterns = [
    path('', login_required(DashboardHomeList.as_view(), login_url=login_url), name="dashboard-home"),
    path('add/', login_required(DashboardAddCrypto.as_view(), login_url=login_url), name="dashboard-add"),

    path('transaction/add', login_required(TransactionCreate.as_view(), login_url=login_url),
         name="add-transaction"),
    path('transaction/<int:pk>/edit', login_required(TransactionUpdate.as_view(), login_url=login_url),
         name="edit-transaction"),
    path('transaction/<int:pk>/delete', login_required(TransactionDelete.as_view(), login_url=login_url),
         name="delete-transaction"),
    path('transaction/<int:pk>/detail', login_required(TransactionDetail.as_view(), login_url=login_url),
         name="detail-transaction"),

    path('transactions', login_required(TransactionsList.as_view(), login_url=login_url), name="list-transactions"),

    path('wallets', login_required(WalletsList.as_view(), login_url=login_url), name="list-wallets"),

    path('assets', login_required(HoldingsList.as_view(), login_url=login_url), name="list-assets"),

    path('currencies', login_required(CurrenciesList.as_view(), login_url=login_url), name="list-currencies"),

    # path('add-bank/', login_required(BrokerApiCreate.as_view(), login_url='home'), name="dashboard-add-bank"),
]
