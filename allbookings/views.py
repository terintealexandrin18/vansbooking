from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import BookingRequest

from django.contrib.auth.decorators import login_required
from .forms import BookingForm

@login_required
def make_booking(request):
    """
    Renders the form to make a booking.

    **Context**
    ``booking_form``
        An instance of :form:`allbookings.BookingForm`.

    **Template**
    :template:`allbookingapp/make_the_bookings.html`
    """
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            existing_booking = BookingRequest.objects.filter(user=request.user, date=booking_form.cleaned_data['date'], time_slot=booking_form.cleaned_data['time_slot']).exists()
            if existing_booking:
                booking_form.add_error(None, 'Sorry, but the time slot you selected is no longer available. Please choose a different time slot that suits your schedule.')
            else:
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

@login_required
def booking_edit(request, booking_id):
    """
    Renders the page for editing a booking.

    Gets the specific :model:`allbookings.BookingRequest` instance by booking_id.

    **Context**
    ``booking_form``
        An instance of :form:`allbookings.BookingForm`.

    **Template**
    :template:`allbookingapp/edit_the_bookings.html`
    """
    booking = get_object_or_404(BookingRequest, pk=booking_id)
    booking_form = BookingForm(request.POST or None, instance=booking)
    
    if request.method == "POST":
        if booking_form.is_valid() and booking.user == request.user:
            existing_booking = BookingRequest.objects.filter(user=request.user, date=booking_form.cleaned_data['date'], time_slot=booking_form.cleaned_data['time_slot']).exclude(id=booking_id).exists()
            if existing_booking:
                booking_form.add_error(None, 'Sorry, but the time slot you selected is no longer available. Please choose a different time slot that suits your schedule.')
            else:
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
    Renders the confirmation page for deleting a booking.

    Gets the specific :model:`allbookings.BookingRequest` instance by booking_id.

    **Context**
    ``booking``
        An instance of :model:`allbookings.BookingRequest`.

    **Template**
    :template:`allbookingapp/delete_the_booking.html`
    """
    booking = get_object_or_404(BookingRequest, pk=booking_id)

    if booking.user == request.user:
        if request.method == 'POST':
            booking.delete()
            messages.success(request, 'Booking deleted!')
            return redirect('view-the-booking') 
        else:
            return render(request, 'allbookings/delete_the_bookings.html', {'booking': booking})
    else:
        messages.error(request, 'You can only delete your own bookings!')
        return redirect('view-the-booking')
