from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from allbookings.models import BookingRequest

class TestViewBooking(TestCase):

    def setUp(self):
        """Creates a user and some bookings for testing."""
        self.user = User.objects.create_user(username='test11', password='12345')
        self.client = Client()
        self.client.login(username='test11', password='12345')
        self.booking1 = BookingRequest.objects.create(user=self.user, choose_a_services='Waste', time_slot='7:00', date='2024-04-15')
        self.booking2 = BookingRequest.objects.create(user=self.user, choose_a_services='Transfer', time_slot='9:00', date='2024-04-16')

    def test_view_booking(self):
        """Test to verify the view_booking view."""
        response = self.client.get(reverse('view-the-booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewthebooking/view_the_booking.html')
        expected_queryset = BookingRequest.objects.filter(user=self.user).order_by('created_at')
        context_queryset = response.context['bookings'].order_by('created_at')
        self.assertQuerysetEqual(context_queryset, expected_queryset)