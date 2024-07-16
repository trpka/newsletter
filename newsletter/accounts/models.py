from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)


class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    subscribers = models.ManyToManyField(
        Company, related_name="subscribed_companies", blank=True
    )
    address = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
