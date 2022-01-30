from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DetailView

from accounts.forms import UserRegistrationForm, UserChangeAccountForm
from accounts.models import CustomUser


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/login.html", context={"form": form})


class AccountsHomeNoConnect(DetailView):
    model = CustomUser
    form_class = AuthenticationForm
    template_name = "accounts/home-account.html"
    context_object_name = "form-login"
    success_url = reverse_lazy('dashboard-home')
    success_message = 'Login success'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form-creation'] = UserCreationForm
        return context


class AccountsEdit(UpdateView):
    model = CustomUser
    form_class = UserChangeAccountForm
    template_name = "accounts/edit-account.html"
    success_url = reverse_lazy('dashboard-home')
    success_message = 'Update success'
