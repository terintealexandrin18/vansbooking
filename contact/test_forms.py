from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields being valid """
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '01234567890',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_first_name_is_required(self):
        """Test for the 'first_name' field being required"""
        form = ContactForm({
            'first_name': '',
            'last_name': 'Ter',
            'contact_number': '01234567890',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="First name was not provided, but the form is valid"
        )

    def test_last_name_is_required(self):
        """Test for the 'last_name' field being required"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': '',
            'contact_number': '01234567890',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Last name was not provided, but the form is valid"
        )

    def test_contact_number_is_required(self):
        """Test for the 'contact_number' field being required"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Contact number was not provided, but the form is valid"
        )

    def test_contact_number_is_11_digits(self):
        """Test for the 'contact_number' field being exactly 11 digits"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '0123456789',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Contact number with 10 digits is invalid, but the form is valid"
        )
        self.assertIn('contact_number', form.errors, msg="Error should be in contact_number field")
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '012345678901',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Contact number with 12 digits is invalid, but the form is valid"
        )
        self.assertIn('contact_number', form.errors, msg="Error should be in contact_number field")
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

    def test_contact_number_is_numeric(self):
        """Test for the 'contact_number' field being numeric"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '01234abc890',
            'email': 'alex@example.com',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Contact number with letters is invalid, but the form is valid"
        )
        self.assertIn('contact_number', form.errors, msg="Error should be in contact_number field")
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

    def test_email_is_required(self):
        """Test for the 'email' field being required"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '01234567890',
            'email': '',
            'message': 'Test test Test!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field being required"""
        form = ContactForm({
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '01234567890',
            'email': 'alex@example.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
