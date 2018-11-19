from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=50, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='users', null=True)
