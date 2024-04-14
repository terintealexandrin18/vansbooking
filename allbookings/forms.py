from django import forms
from .models import BookingRequest

class BookingForm(forms.ModelForm):
    """
    Form for creating or updating a booking request.

    **Model**
    :model:`allbookings.BookingRequest`

    **Template**
    - For creating a booking: :template:`allbookings/make_the_bookings.html`
    - For updating a booking: :template:`allbookings/edit_the_bookings.html`
    """
    class Meta:
        model = BookingRequest 
        fields = ['contact_number', 'date', 'time_slot', 'choose_a_services', 'comments']
        widgets = {
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'value': ''}),
            'comments': forms.Textarea(attrs={'placeholder': 'Please provide the additional requirements.'})
        }
