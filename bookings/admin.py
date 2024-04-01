from django.contrib import admin
from  .models import HomePage, Image
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(HomePage)
class HomePageAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')

admin.site.register(Image)


