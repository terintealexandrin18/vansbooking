from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import BookingRequest
from .forms import BookingForm


class MakeBookingViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='test_user',
                                            password='test_password')

    def test_make_booking_view_GET(self):
        # Test the GET request to the make booking view
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse('make_the_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'allbookings/make_the_bookings.html')
        self.assertIsInstance(response.context['booking_form'], BookingForm)

    def test_make_booking_view_POST_valid_form(self):
        # Test POST request with a valid form submission for making a booking
        client = Client()
        client.force_login(self.user)
        post_data = {
            'contact_number': '123456789',
            'date': '2024-04-13',
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        }
        response = client.post(reverse('make_the_bookings'), data=post_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('view-the-booking'))
        self.assertTrue(BookingRequest.objects.filter(user=self.user,
                        contact_number='123456789', date='2024-04-13',
                        time_slot='7:00 - 8:30',
                        choose_a_services='Waste Collection',
                        comments='Test comments').exists())


class BookingEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user and booking request for editing
        cls.user = User.objects.create_user(username='test11',
                                            password='12345')
        cls.booking_request = BookingRequest.objects.create(
            user=cls.user,
            contact_number='123456789',
            date='2024-04-13',
            time_slot='7:00 - 8:30',
            choose_a_services='Waste Collection',
            comments='Test comments'
            )

    def test_booking_edit_view_GET(self):
        # Test the GET request to the edit booking view
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse('edit-booking',
                                      args=[self.booking_request.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'allbookings/edit_the_bookings.html')
        self.assertIsInstance(response.context['booking_form'], BookingForm)
        self.assertEqual(response.context['booking_form'].instance,
                         self.booking_request)


class BookingDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user and booking request for deletion
        cls.user = User.objects.create_user(username='test11',
                                            password='12345')
        cls.booking_request = BookingRequest.objects.create(
            user=cls.user, contact_number='123456789', date='2024-04-13',
            time_slot='7:00 - 8:30', choose_a_services='Waste Collection',
            comments='Test comments'
            )

    def test_booking_delete_view_GET(self):
        # Test the GET request to the delete booking view
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse('delete-booking',
                                      args=[self.booking_request.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'allbookings/delete_the_bookings.html')
        self.assertEqual(response.context['booking'], self.booking_request)
