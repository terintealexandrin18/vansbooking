from django import forms
from django.core.exceptions import ValidationError
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

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit() or len(contact_number) != 11:
            raise ValidationError('Enter a valid 11-digit contact number.')
        return contact_number

    class Meta:
        model = BookingRequest
        fields = ['contact_number', 'date', 'time_slot', 'choose_a_services', 'comments']
        widgets = {
            'contact_number': forms.TextInput(attrs={'placeholder': '01234567891'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'comments': forms.Textarea(attrs={'placeholder': 'Please provide the additional requirements.'}),
        }
