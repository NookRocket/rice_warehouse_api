# from django.db import models
from django.contrib.auth.models import AbstractUser
from djongo import models

# Create your models here.
class User(AbstractUser):
    """custom user model"""
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
