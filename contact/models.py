from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    """
    Model representing a contact message.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    read = models.BooleanField(default=False)
