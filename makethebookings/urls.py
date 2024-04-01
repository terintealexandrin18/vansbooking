from . import views
from django.urls import path

urlpatterns = [
    path('make-the-bookings/', views.make_booking, name='make_the_bookings'),
    
]