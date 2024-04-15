from django import forms
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
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'contact_number',
                  'email', 'message']
