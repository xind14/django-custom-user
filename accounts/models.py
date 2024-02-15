from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=160, unique=True)
    username = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username