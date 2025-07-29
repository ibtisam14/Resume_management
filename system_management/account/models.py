from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
