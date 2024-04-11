from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class HomePage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.title

class Image(models.Model):
    home_page = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Image for {self.home_page.title}"