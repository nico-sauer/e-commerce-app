from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ()
    username = None
    email = models.EmailField(("email address"), unique=True)
    
    def __str__(self):
        return self.email