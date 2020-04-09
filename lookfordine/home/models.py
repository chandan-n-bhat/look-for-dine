from django.db import models

# Create your models here.

class SpecialityMenu(models.Model):

    cuisineName = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=1000)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.cuisineName

class Branch(models.Model):

    manager = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.address + ', ' + self.city + ', ' + self.state 
    
class About(models.Model):

    name = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    founded = models.DateField()

    def __str__(self):
        return self.name