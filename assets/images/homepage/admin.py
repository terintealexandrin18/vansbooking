from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import HomePage, Image


# Register your models here.
@admin.register(HomePage)
class HomePageAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the HomePage model.
    It enables Summernote rich text editor for the content field.
    """
    summernote_fields = ('content')


admin.site.register(Image)
