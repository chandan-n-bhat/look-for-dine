from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):

    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=20)
    people = models.IntegerField()
    datetime = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

    def __str__(self):
        return "Booking:" + self.name + " - " + self.datetime