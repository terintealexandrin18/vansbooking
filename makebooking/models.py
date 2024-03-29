from django.db import models

# Create your models here.

class BookingRequest(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    TIME_CHOICES = [
        ('7AM', '7:00 - 8:30'),
        ('9AM', '9:00 - 10:30'),
        ('11AM', '11:00 - 12:30'),
        ('1PM', '13:00 - 14:30'),
        ('3PM', '15:00 - 16:30'),
        ('5PM', '17:00 - 18:30'),
    ]

    SERVICE_CHOICES = [
        ('Waste Collection', 'Waste Collection'),
        ('Site-to-Site Transfer', 'Site-to-Site Transfer'),
        ('Van and Driver Hire', 'Van and Driver Hire'),
        ('Additional Services - Write the details in Comments section', 'Additional Services - Write the details in Comments section'),
        
    ]

    username = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=20)
    days_of_week = models.CharField(max_length=100, choices=DAY_CHOICES)
    time_slot = models.CharField(max_length=100, choices=TIME_CHOICES)
    choose_a_services = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    comments = models.TextField()
    uk_postcodes = models.CharField(max_length=100, blank=True, null=True)