from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


@login_required
def dashboard(request):
    return HttpResponse("Yo le dashboard")
