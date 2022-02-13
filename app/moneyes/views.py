from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return render(request, "index.html")

    else:
        response = redirect('login')
        return response


