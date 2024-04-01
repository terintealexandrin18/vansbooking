from . import views
from django.urls import path

urlpatterns = [
    path('make-booking/', views.make_booking, name='make_booking'),
    
]