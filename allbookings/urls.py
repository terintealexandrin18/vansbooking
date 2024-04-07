from . import views
from django.urls import path

urlpatterns = [
    path('make-the-bookings/', views.make_booking, name='make_the_bookings'),
    path('edit-the-bookings/<int:booking_id>/', views.booking_edit, name='edit-booking'),
    path('delete-the-bookings/<int:booking_id>/', views.booking_delete, name='delete-booking'),
    
]
