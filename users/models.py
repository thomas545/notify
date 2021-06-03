from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """

    phone_number = models.CharField(max_length=25, blank=True, null=True, unique=True)
