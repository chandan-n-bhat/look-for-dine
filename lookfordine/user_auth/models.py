from django.db import models
from django.contrib.auth.models import User
import jsonfield

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(blank=True)
    recommendation = jsonfield.JSONField()
    personalised_menu = jsonfield.JSONField()    

    def __str__(self):

        return self.user.username
