from django.shortcuts import render

# Create your views here.

def make_booking(request):


    return render(request, 'bookings/make_booking.html')