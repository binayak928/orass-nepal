import datetime
from django.db import models
# Create your models here.
from django.utils import timezone


class DonationsDemo(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    amt = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s %s' % (self.name, self.date, self.amt)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s %s %s %s %s' % (self.title, self.category, self.author, self.body, self.post_date)


class Event(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    title = models.CharField(max_length=255)
    address_street = models.CharField(max_length=255)
    address_city = models.CharField(max_length=100)
    address_country = models.CharField(max_length=100)
    description = models.TextField()
    organizer = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    picture = models.ImageField(null=True, blank=True, upload_to="events/")

    def __str__(self):
        return '%s %s' % (self.date, self.title)
