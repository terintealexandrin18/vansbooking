from django.shortcuts import render
from .models import HomePage

# Create your views here.

def home(request):
    home_pages = HomePage.objects.all().order_by('-updated_on')
    return render(
        request,
        "bookings/index.html",
        {"home_pages": home_pages},
    )