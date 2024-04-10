from django.contrib import admin
from .models import ContactMessage

# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact_number', 'email', 'message', 'created_at']
    list_filter = ['read']
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)
    mark_as_read.short_description = "Mark selected messages as read"
