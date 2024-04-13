from django.test import TestCase, Client
from django.urls import reverse
from .views import home
from .models import HomePage


class HomePageViewTest(TestCase):
    """Test for the home view."""
    @classmethod
    def setUpTestData(cls):
        HomePage.objects.create(title='Title 1', content='Content 1')
        HomePage.objects.create(title='Title 2', content='Content 2')

    def test_home_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')
        self.assertIn('home_pages', response.context)
        self.assertEqual(len(response.context['home_pages']), HomePage.objects.count())