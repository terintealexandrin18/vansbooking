from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class HomePage(models.Model):
    """
    Model representing a homepage content.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)


class Image(models.Model):
    """
    Model representing images associated with the homepage.
    """
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    image = CloudinaryField('image')
