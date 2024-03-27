from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('make-booking/', views.make_booking, name='make_booking'),
]