
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

ADMINISTRATOR, USER = ("administrator", "user")

class User(AbstractUser):
    ROLE_CHOICES = (
        (ADMINISTRATOR, ADMINISTRATOR),
        (USER, USER),
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=USER)








