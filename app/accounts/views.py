from datetime import date

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, TemplateView

from accounts.forms import UserChangeAccountForm, SignUpForm, LogInForm
from accounts.models import CustomUser
from dashboard.models import Account


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=user.email, password=raw_password)
            login(request, user)
            today = date.today()
            Account.objects.create(user=user, created=today, updated=today)
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "registration/login.html", context={"form": form})


def logout(request):
    logout(request)
    return redirect("home")


class LogIn(TemplateView):
    model = CustomUser
    form_class = LogInForm
    template_name = "accounts/home-account.html"
    context_object_name = "form_login"
    success_url = reverse_lazy('dashboard-home')
    success_message = 'Login success'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_creation'] = 
        return context


class AccountsEdit(UpdateView):
    model = CustomUser
    form_class = UserChangeAccountForm
    template_name = "accounts/edit-account.html"
    success_url = reverse_lazy('dashboard-home')
    success_message = 'Update success'
