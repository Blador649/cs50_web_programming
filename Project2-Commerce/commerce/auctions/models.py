from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listings(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    current_price = models.DecimalField(max_digits=2)
    image_url = models.URLField()
    # create_user = models.CharField(max_length=100)
    # date_created = models.Date()
    
class Bids(models.Model):
    pass

class Comments(models.Model):
    pass