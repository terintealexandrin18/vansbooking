from datetime import date
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BookingRequest(models.Model):
    """
    Represents a booking request made by a user.
    """
    
    TIME_CHOICES = [
        ('7:00 - 8:30', '7:00 - 8:30'),
        ('9:00 - 10:30', '9:00 - 10:30'),
        ('11:00 - 12:30', '11:00 - 12:30'),
        ('13:00 - 14:30', '13:00 - 14:30'),
        ('15:00 - 16:30', '15:00 - 16:30'),
        ('17:00 - 18:30', '17:00 - 18:30'),
    ]

    SERVICE_CHOICES = [
        ('Waste Collection', 'Waste Collection'),
        ('Site-to-Site Transfer', 'Site-to-Site Transfer'),
        ('Van and Driver Hire', 'Van and Driver Hire'),
        ('Additional Services - Write the details in Comments section', 'Additional Services - Write the details in Comments section'),  
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact_number = models.CharField(max_length=12, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    time_slot = models.CharField(max_length=100, choices=TIME_CHOICES, blank=False, null=False)
    choose_a_services = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    comments = models.TextField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
