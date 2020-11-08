from django.db import models


# Create your models here.
class DonationsDemo(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    amt = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s %s' % (self.name, self.date, self.amt)
