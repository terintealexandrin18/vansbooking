from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allbookings.models import BookingRequest

# Create your views here. 

@login_required
def view_booking(request):
    bookings = BookingRequest.objects.filter(user=request.user)
    return render(request, 'viewthebooking/view_the_booking.html', {'bookings':bookings})