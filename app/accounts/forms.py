from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", )


class UserChangeAccountForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "name",
            "last_name",
        )