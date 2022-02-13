from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class LogInForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
        )


class UserChangeAccountForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "name",
            "last_name",
        )
