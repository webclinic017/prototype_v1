from django.contrib.auth.forms import UserCreationForm

from src.accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("emails", )