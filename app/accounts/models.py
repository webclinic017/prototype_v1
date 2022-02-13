from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, last_name, password=None):
        if not email:
            raise ValueError('Put Email Address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            name=name,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True,
        max_length=255,
        blank=False
    )
    name = models.CharField(
        max_length=125,
        null=True,
    )
    last_name = models.CharField(
        max_length=125,
        null=True,
    )
    #thumbnail = models.ImageField(
    #    blank=True,
    #    upload_to='thumbnails'
    #)
    # User for admin interface
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    zip_code = models.CharField(blank=True, max_length=5)

    USERNAME_FIELD = "email"
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
