

import datetime

from django.conf import settings
from django.core.validators import RegexValidator, EmailValidator
from django.db import models
from django.utils.timezone import now as datetime_now
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, first_name=None, last_name=None):
        """
        Creates and saves a user with given email and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model that only requires an email and password"""
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True) 

    # required for admin
    is_active = models.BooleanField(
        default=True,
        help_text="Designates that this user account should be considered active. Users marked as inactive cannot login."
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates that this user can access the admin site.",
    )

    date_joined = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)

    # if True, a user can edit membership
    is_manager = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else self.email


    def get_short_name(self):
        return self.first_name if self.first_name else self.email

    @property
    def name(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()