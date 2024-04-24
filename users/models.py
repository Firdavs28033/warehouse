
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.core.validators import FileExtensionValidator

ADMINISTRATOR, USER = ("administrator", "user")

class User(AbstractUser):
    ROLE_CHOICES = (
        (ADMINISTRATOR, ADMINISTRATOR),
        (USER, USER),
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default=USER)
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/",
                                        default="/cover_pic/nopic.jpg", blank=True, null=True,
                                        validators=[FileExtensionValidator(["jpg", "png", "jpeg", "heic"])])


    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"







