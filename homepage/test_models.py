from django.test import TestCase
from .models import HomePage, Image
from django.utils import timezone


class HomePageModelTest(TestCase):
    """Test cases for the HomePage model."""

    @classmethod
    def setUpTestData(cls):
        HomePage.objects.create(title='Test HomePage', content='Test content')

    def test_updated_on_auto_now(self):
        home_page = HomePage.objects.get(id=1)
        current_time = timezone.now()
        self.assertLessEqual((current_time - home_page.updated_on)
                             .total_seconds(), 1)


class ImageModelTest(TestCase):
    """Test cases for the Image model."""

    @classmethod
    def setUpTestData(cls):
        home_page = HomePage.objects.create(title='Test HomePage',
                                            content='Test content')
        Image.objects.create(home_page=home_page, image='test_image.jpg')

    def test_home_page_foreign_key(self):
        image = Image.objects.get(id=1)
        self.assertEquals(image.home_page.title, 'Test HomePage')

    def test_image_field(self):
        image = Image.objects.get(id=1)
        self.assertIsNotNone(image.image)
