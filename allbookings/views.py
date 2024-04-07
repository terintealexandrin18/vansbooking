from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
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
            return HttpResponseRedirect(reverse('view-the-booking'))

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
    booking = get_object_or_404(BookingRequest, pk=booking_id)
    booking_form = BookingForm(request.POST or None, instance=booking)
    
    if request.method == "POST":
        if booking_form.is_valid() and booking.user == request.user:
            updated_booking = booking_form.save(commit=False)
            if updated_booking.status == 'approved':
                updated_booking.status = 'pending'
            updated_booking.save()
            messages.success(request, 'Booking Updated!')
            return HttpResponseRedirect(reverse('view-the-booking'))
        else:
            messages.error(request, 'Error updating booking!')

    return render(
        request,
        "allbookings/edit_the_bookings.html",
        {"booking_form": booking_form},
    )

@login_required
def booking_delete(request, booking_id):
    """
    Delete an individual booking request.

    **Context**

    ``booking``
        An instance of :model:`allbookings.BookingRequest`.
    """
    booking = get_object_or_404(BookingRequest, pk=booking_id)

    if booking.user == request.user:
        if request.method == 'POST':
            booking.delete()
            messages.success(request, 'Booking deleted!')
            return redirect('view-the-booking')  # Redirect to desired URL after successful deletion
        else:
            return render(request, 'allbookings/delete_the_bookings.html', {'booking': booking})
    else:
        messages.error(request, 'You can only delete your own bookings!')
        return redirect('view-the-booking')
