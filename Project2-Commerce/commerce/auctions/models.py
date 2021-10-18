from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"


class Listing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    fl_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(null=True, max_length=300)
    starting_bid = models.FloatField()
    current_bid = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="similar_listings")
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="all_creators_listings")
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_listings")
    buyer = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} - {self.starting_bid}"


class Bid(models.Model):
    auction = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.FloatField()
    date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_comments")

    def get_creation_date(self):
        return self.created_date.strftime('%B %d %Y')


class Picture(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_pictures")
    picture = models.ImageField(upload_to="images/")
    alt_text = models.CharField(max_length=140)