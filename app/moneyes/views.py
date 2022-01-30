from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated:
        response = redirect('/dashboard/')
        return response

    else:
        form_login = AuthenticationForm()
        form_creation = UserCreationForm()
        context = {
            "form_login": form_login,
            "form_creation": form_creation,
        }

    return render(request, "accounts/home-account.html", context=context)
