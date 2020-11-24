import datetime

from django.db import models


# Create your models here.
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
    post_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return '%s %s %s %s %s' % (self.title, self.category, self.author, self.body, self.post_date)
