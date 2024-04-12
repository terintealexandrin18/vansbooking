from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allbookings.models import BookingRequest

# Create your views here. 

@login_required
def view_booking(request):
    """
    View function to display the bookings associated with the currently logged-in user.

    **Context:**
    - ``bookings`` (QuerySet): A queryset of BookingRequest objects associated with the current user.

    **Template:**
    - Renders the 'view_the_booking.html' template, which displays the bookings.

    **Requires authentication:**
    - Users must be logged in to access this view.

    **Foreign Key Relationship:**
    - The BookingRequest model has a ForeignKey relationship with the User model.

    **Returns:**
    - Rendered response containing the booking information for the current user.
    """
    
    bookings = BookingRequest.objects.filter(user=request.user)
    return render(request, 'viewthebooking/view_the_booking.html', {'bookings':bookings})