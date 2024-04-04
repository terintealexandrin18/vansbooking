from django import forms
from .models import BookingRequest

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest 
        fields = ['contact_number', 'date', 'time_slot', 'choose_a_services', 'comments']
