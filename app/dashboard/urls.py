from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import DashboardHomeList, DashboardAddCrypto, TransactionCreate, TransactionUpdate, TransactionDelete, \
    TransactionDetail, TransactionsList

urlpatterns = [
    path('', login_required(DashboardHomeList.as_view(), login_url='home'), name="dashboard-home"),
    path('add/', login_required(DashboardAddCrypto.as_view(), login_url='home'), name="dashboard-add"),

    path('transaction/add', login_required(TransactionCreate.as_view(), login_url='home'), name="dashboard-add-transaction"),
    path('transaction/<int:pk>/edit', login_required(TransactionUpdate.as_view(), login_url='home'), name="edit-transaction"),
    path('transaction/<int:pk>/delete', login_required(TransactionDelete.as_view(), login_url='home'), name="delete-transaction"),
    path('transaction/<int:pk>/detail', login_required(TransactionDetail.as_view(), login_url='home'), name="detail-transaction"),

    path('transactions', login_required(TransactionsList.as_view(), login_url='home'), name="list-transactions"),


    
    #path('add-bank/', login_required(BrokerApiCreate.as_view(), login_url='home'), name="dashboard-add-bank"),
]
