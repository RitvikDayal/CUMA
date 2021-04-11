# Django utility imports
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Django default model extentions
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):
    '''Custom user manager
    A custom account manager to handle user and super user account creations.
    
    Functions: 
        - create_user : to handle creation of a default user account
        - create_superuser : to handle creation of super_user account
    '''
    def create_user(self, email, user_name, first_name, password, **other_fields):
        '''
        This manager creates a simple user account for the given email.
        '''
        if not email:
            raise ValueError(_('You must provide an email address.'))

        # cleaning mail address.
        email = self.normalize_email(email)

        # creating user model object        
        user = self.model(email=email, user_name=user_name, first_name=first_name, password=password, **other_fields)
        
        # setting password for the user
        user.set_password(password)
        
        # saving user model instance
        user.save()
        
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        '''
        This manager creates a super user account for the given email.
        '''

        # setting superuser, staff, active status as true by default
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        # checking for staff status
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')

        #checking for superuser status
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True.')

        # Creating user account for superuser.
        return self.create_user(email, user_name, first_name, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom user model
    '''
    email = models.EmailField(_('Email Address'), unique=True)
    user_name = models.CharField(_('Username'), max_length=150, unique=True)
    first_name = models.CharField(_('First Name'), max_length=150)
    last_name = models.CharField(_('Last Name'), max_length=150)
    created_on = models.DateTimeField(_('Account Created on'), default=timezone.now)
    about = models.TextField(_('About'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    # Mentioning the attribute to be used for login instead of username
    USERNAME_FIELD = 'email'

    # Fields required to be field during user registration
    REQUIRED_FIELDS = ['user_name', 'first_name']

    # Custom user account Manager class
    objects = CustomUserManager()
    
    def __str__(self):
        return self.user_name

