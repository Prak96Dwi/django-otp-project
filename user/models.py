""" apps/user/models.py
This module contains some non-abstract classes
    * class : Customer
    * class : Profile
"""

# Core Django modules
from django.db import models
from django.contrib.auth.models import  (
    AbstractBaseUser, BaseUserManager
)
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Native app modules
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser):
    """
    Table of Customer model inheriting AbstractUser
    """
    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    # Full name of a registered user
    full_name = models.CharField(
        max_length=259,
        help_text=_("Full Name"),
        null=True
    )

    # Email of a registered user
    email = models.EmailField(
        max_length=50,
        unique=True,
        help_text=_("Email")
    )

    # Address of a registered user
    address = models.CharField(
        max_length=500,
        null=True,
        help_text=_("Address")
    )

    # # User phone number
    # phone = models.CharField(
    #     blank=True,
    #     null=True,
    #     max_length=50,
    #     help_text=_("Contact phone number")
    # )

    # type = models.CharField(max_length=50, null=False, help_text=_("User Type"))
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    #======================================================================================
    def get_short_name(self) -> str:
        # The user is identified by their email address
        return self.email

    def __str__(self) -> str:
        """ string representation of Customer instance """
        return f'{self.full_name}'

    def save(self, *args, **kwargs): # pylint: disable=arguments-differ
        """
        save cleaned data of user object
        """
        # self.full_clean()
        super().save(*args, **kwargs)

    #========================================================================================
    def has_perm(self, perm, obj=None) -> bool:
        """ has permission """
        return self.is_admin

    def has_module_perms(self, app_label) -> str:
        """ has module permission """
        return self.is_admin

