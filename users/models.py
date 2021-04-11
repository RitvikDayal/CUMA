from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, user_name, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('You must provide an email address.'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, first_name=first_name, password=password, **other_fields)
        
        user.set_password(password)
        
        user.save()
        
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('Email Address'), unique=True)
    user_name = models.CharField(_('Username'), max_length=150, unique=True)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150)
    created_on = models.DateTimeField(_('Account Created on'), default=timezone.now)
    about = models.TextField(_('About'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['user_name', 'first_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.user_name

