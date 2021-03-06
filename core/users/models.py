from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Stores a custom user model, based on a UUID pk, username is desactived and we
    use an email for :model:`core.users.CustomUser`. We keep in place the firstname and lastname.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
