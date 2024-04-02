from . import views
from django.urls import path

urlpatterns = [
    path('view-the-booking/', views.view_booking, name='view-the-booking'),
]