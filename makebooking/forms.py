from django import forms
from .models import BookingRequest

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest 
        fields = ['contact_number', 'days_of_week', 'time_slot', 'services', 'comments']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['username'] = forms.CharField(initial=user.username, widget=forms.HiddenInput())