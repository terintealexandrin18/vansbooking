
from django.test import TestCase, Client
from django.urls import reverse
from .forms import ContactForm

class TestContactUsView(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_render_contact_form(self):
        """Test GET request for rendering contact form."""
        response = self.client.get(reverse('contact_us'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertFalse(response.context['submitted'])

    def test_successful_message_submission(self):
        """Test POST request for submitting a message."""
        post_data = {
            'first_name': 'Alex',
            'last_name': 'Ter',
            'contact_number': '1234567890',
            'email': 'alex@example.com',
            'message': 'Testtest Test!'
        }
        response = self.client.post(reverse('contact_us'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertTrue(response.context['submitted'])
        self.assertContains(response, 'Your message has been sent successfully!')