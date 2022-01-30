from django.contrib.auth.decorators import login_required
from django.urls import path, include

from accounts.views import signup, AccountsEdit

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name="login"),
    path('signup/', signup, name="signup"),
    path('<int:pk>/edit', login_required(AccountsEdit.as_view(), login_url='home'), name="account-edit"),
]
