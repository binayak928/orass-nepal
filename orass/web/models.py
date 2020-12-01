from django.db import models
# Create your models here.
from django.utils import timezone


class DonationsDemo(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    amt = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s %s' % (self.name, self.date, self.amt)


class HomePageFund(models.Model):
    raised = models.IntegerField()
    goal = models.IntegerField()
    percentage = models.IntegerField(null=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    body = models.TextField()
    post_date = models.DateField(default=timezone.now)
    picture = models.ImageField(upload_to='blog/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.title, self.post_date)


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
    picture = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.date, self.title)


class EventParticipation(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    message = models.CharField(max_length=255, null=True, blank=True)
    regDate = models.DateField(auto_now_add=True)
    eventDate = models.DateField()
    title = models.CharField(max_length=255)


class InterestedDonor(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    nationality = models.CharField(max_length=70)

    def __str__(self):
        return '%s %s' % (self.date, self.email)


class ContactForm(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return '%s %s' % (self.date, self.email)
