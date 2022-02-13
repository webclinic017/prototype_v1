from django.contrib.auth.decorators import login_required
from django.urls import path, include
from accounts.views import AccountsEdit, logout, signup, loginUser, change_password
from moneyes import settings

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('login/', loginUser, name="login"),
    path('logout/', logout, {"next_page": settings.LOGOUT_REDIRECT_URL}, name="account-logout"),

    path('signup/', signup, name="signup"),
    path('password/', change_password, name="change-password"),
    path('<int:pk>/edit', login_required(AccountsEdit.as_view(), login_url='home'), name="account-edit"),
]