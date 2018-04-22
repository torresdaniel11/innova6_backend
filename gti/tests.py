from django.test import TestCase
from django.test.client import Client

from .models import Category

import json


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(category_name="lion")
        Category.objects.create(category_name="cat")

    def test_categories_can_speak_get_all(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/categories/')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2
