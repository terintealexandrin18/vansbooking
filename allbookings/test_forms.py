from django.test import TestCase
from .forms import BookingForm
from datetime import date, timedelta

class BookingFormTest(TestCase):

    def test_valid_contact_number(self):
        form = BookingForm(data={
            'contact_number': '01234567890',
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertTrue(form.is_valid())

    def test_contact_number_with_letters(self):
        form = BookingForm(data={
            'contact_number': '01234abc890',
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

    def test_contact_number_too_short(self):
        form = BookingForm(data={
            'contact_number': '012345',
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

    def test_contact_number_too_long(self):
        form = BookingForm(data={
            'contact_number': '012345678901',
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

    def test_contact_number_with_special_characters(self):
        form = BookingForm(data={
            'contact_number': '01234!@#890',
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_number'], ['Enter a valid 11-digit contact number.'])

    def test_valid_date(self):
        form = BookingForm(data={
            'contact_number': '01234567890',
            'date': (date.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertTrue(form.is_valid())

    def test_past_date(self):
        form = BookingForm(data={
            'contact_number': '01234567890',
            'date': (date.today() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['date'], ['Enter a date that is not in the past.'])

    def test_future_date(self):
        form = BookingForm(data={
            'contact_number': '01234567890',
            'date': (date.today() + timedelta(days=30)).strftime('%Y-%m-%d'),
            'time_slot': '7:00 - 8:30',
            'choose_a_services': 'Waste Collection',
            'comments': 'Test comments'
        })
        self.assertTrue(form.is_valid())
