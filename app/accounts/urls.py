from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.contrib.auth import urls
from accounts.views import signup, AccountsEdit, LogIn, logout
from moneyes import settings

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('login/', LogIn.as_view(), name="login"),
    path('logout/', logout, {"next_page": settings.LOGOUT_REDIRECT_URL}, name="account-logout"),

    path('signup/', signup, name="signup"),
    path('<int:pk>/edit', login_required(AccountsEdit.as_view(), login_url='home'), name="account-edit"),
]
