from django.shortcuts import render
from .models import HomePage

# Create your views here.

def home(request):
    home_page = HomePage.objects.all().order_by('-updated_on').first()
    return render(
        request,
        "bookings/index.html",
        {"home_page": home_page},
    )