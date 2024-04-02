from django.contrib import admin
from .models import BookingRequest

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'contact_number', 'date', 'time_slot', 'choose_a_services', 'comments', 'status', 'created_at')
    list_filter = ('status',)
    actions = ['approve_requests', 'cancel_requests']

    def get_username(self, obj):
        return obj.user.username if obj.user else ''
    get_username.short_description = 'User'

    def approve_requests(self, request, queryset):
        queryset.update(status='approved')
        self.message_user(request, "Selected requests have been approved.")

    def cancel_requests(self, request, queryset):
        queryset.update(status='cancelled')
        self.message_user(request, "Selected requests have been cancelled.")
    
    approve_requests.short_description = "Approve selected requests"
    cancel_requests.short_description = "Cancel selected requests"