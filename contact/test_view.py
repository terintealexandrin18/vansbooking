from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactForm

class TestContactUsView(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('contact_us')

    def test_successful_message_submission(self):
        """Test POST request for submitting a valid message."""
        form_data = {
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '01234567890',
            'email': 'alex@example.com',
            'message': 'Test message'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['submitted'])
        self.assertTrue(ContactMessage.objects.filter(email='alex@example.com').exists())

    def test_message_submission_invalid_form(self):
        """Test POST request for submitting an invalid message."""
        form_data = {
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '123',
            'email': 'alex@example.com',
            'message': 'Test message'
        }
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context.get('submitted', False))
        self.assertFormError(response, 'form', 'contact_number', 'Enter a valid 11-digit contact number.')
