from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import BookingRequest

from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def make_booking(request):
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.user = request.user
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
        "allbookings/make_the_bookings.html",
        {"booking_form": booking_form},
    )


def booking_edit(request, booking_id):
    """
    Display an individual booking request for edit.

    **Context**

    ``booking``
        An instance of :model:`allbookings.BookingRequest`.
    ``booking_form``
        An instance of :form:`allbookings.BookingForm`
    """
    if request.method == "POST":
        booking = get_object_or_404(BookingRequest, pk=booking_id)
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid() and booking.user == request.user:
            booking = booking_form.save(commit=False)
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'Booking Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating booking!')

    return HttpResponseRedirect(reverse('view-the-booking'))

def booking_delete(request, booking_id):
    """
    Delete an individual booking request.

    **Context**

    ``booking``
        An instance of :model:`allbookings.BookingRequest`.
    """
    booking = get_object_or_404(BookingRequest, pk=booking_id)

    if booking.user == request.user:
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own bookings!')

    return HttpResponseRedirect(reverse('view-the-booking'))