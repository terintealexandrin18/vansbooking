from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class HomePage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title