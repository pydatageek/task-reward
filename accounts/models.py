"""Custom User/Account model and related models"""

from django.contrib.auth.models import (
    AbstractUser, Group as DjangoBaseGroup
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User model"""
    email = models.EmailField(
        _('email address'), unique=True)  # email is required

    def __str__(self):
        if self.first_name or self.last_name:
            return self.get_full_name()
        return self.username


class Group(DjangoBaseGroup):
    """Custom Group Model inherited from Django's default Group model"""
