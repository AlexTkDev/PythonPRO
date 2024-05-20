from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)


class UserProfile(models.Model):
    bio = models.TextField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
