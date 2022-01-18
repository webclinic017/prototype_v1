from django.urls import path, include

from accounts.views import signup

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name="login"),
    path('signup/', signup, name="signup"),
]
