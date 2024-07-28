from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """
    Form class for handling contact message submission.

    Inherits from forms.ModelForm.

    **Model**
    :model:`contact.ContactMessage`

    **Template**
    :template:`contact/contact.html`
    """

    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if not contact_number.isdigit() or len(contact_number) != 11:
            raise ValidationError('Enter a valid 11-digit contact number.')
        return contact_number

    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'message']
        widgets = {
            'contact_number': forms.TextInput(attrs={'placeholder': '01234567891'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your.email@example.com'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...'}),
        }
