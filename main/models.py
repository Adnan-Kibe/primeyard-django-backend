from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
from datetime import timedelta
from django.utils.timezone import now

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, null=True, blank=True) 
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = "primeyard_user"
