from datetime import date

from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, TemplateView

from accounts.forms import UserChangeAccountForm, SignUpForm, LogInForm
from accounts.models import CustomUser
from dashboard.models import Account, Holding


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

    return render(request, "registration/signup.html", context={"form": form})


def loginUser(request):
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LogInForm()

    return render(request, "registration/login.html", context={"form": form})


def logout(request):
    logout(request)
    return redirect("home")


class AccountsEdit(UpdateView):
    model = CustomUser
    form_class = UserChangeAccountForm
    template_name = "accounts/edit-account.html"
    success_url = reverse_lazy('dashboard-home')
    success_message = 'Update success'


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account-edit', pk=user.id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
