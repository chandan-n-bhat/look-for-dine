from django.db import models
import jsonfield
# from django.contrib.auth.models import User
from user_auth.models import Customer

# Create your models here.

class Menu(models.Model):

    cuisineName = models.CharField(max_length=20)
    price = models.CharField(max_length=10)
    cuisineType = models.CharField(max_length=20)
    calories = models.CharField(max_length=10)
    tags = jsonfield.JSONField()
    photo = models.CharField(max_length=100)

    def __str__(self):
        return self.cuisineName

