from django.db import models

# Create your models here.

class Menu(models.Model):
    name    = models.CharField(max_length=200)
    price   = models.IntegerField()
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=100)
    
    def __self__(self):
        return self.first_name + '' + self.last_name
    
    