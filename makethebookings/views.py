from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def make_booking(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(
                request,
                'Your booking request has been submitted successfully!'
            )
            # Clear the form for a new request
            booking_form = BookingForm()
    else:
        booking_form = BookingForm()

    return render(
        request,
        "makethebookings/make_the_bookings.html",
        {"booking_form": booking_form},
    )