from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.user.is_authenticated:
        response = redirect('/dashboard/')
        return response

    else:
        response = redirect('/accounts/login/')
        return response
