from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class actions_user(models.Model):
    username = models.CharField(max_length=64, unique= True)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=254, unique= True)

    USERNAME_FIELD = 'username'
    # def __str__(self):
    #     return self.username