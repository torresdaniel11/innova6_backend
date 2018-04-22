from django.test import TestCase
from rest_framework.test import APIRequestFactory, RequestsClient

from .models import Category


class AnimalTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category_name="lion")
        Category.objects.create(category_name="cat")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Category.objects.get(category_name="lion")
        cat = Category.objects.get(category_name="cat")
        self.assertEqual(lion.category_name, 'lion')
        self.assertEqual(cat.category_name, 'cat')
        factory = APIRequestFactory()
        # request = factory.get('/categories/')
        # category = demo.factories.CategoryFactory.create()
        # self.assertTrue(category.title in response.content)
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/categories/')
        assert response.status_code == 200
