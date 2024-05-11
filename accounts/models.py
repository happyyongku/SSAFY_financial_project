from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user_pk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth = models.DateField()
    capital = models.BigIntegerField()