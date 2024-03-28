from django.db import models

# Create your models here.

class BookingRequest(models.Model):
    username = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=20)
    days_of_week = models.CharField(max_length=100)
    time_slot = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    comments = models.TextField()