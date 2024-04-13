from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '1234567890',
            'email': 'alex@example.com',
            'message': 'Testtest Test!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_first_name_is_required(self):
        """Test for the 'first_name' field"""
        form = ContactForm({
            'first_name': '',
            'last_name': 'Ter',
            'contact_number': '1234567890',
            'email': 'alex@example.com',
            'message': 'Testtest Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="First name was not provided, but the form is valid"
        )

    def test_last_name_is_required(self):
        """Test for the 'last_name' field"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': '',
            'contact_number': '1234567890',
            'email': 'alex@example.com',
            'message': 'Testtest Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Last name was not provided, but the form is valid"
        )

    def test_contact_number_is_required(self):
        """Test for the 'contact_number' field"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '',
            'email': 'alex@example.com',
            'message': 'Testtest Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Contact number was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '1234567890',
            'email': '',
            'message': 'Testtest Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '1234567890',
            'email': 'Alex@example.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )