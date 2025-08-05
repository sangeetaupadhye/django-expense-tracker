from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
