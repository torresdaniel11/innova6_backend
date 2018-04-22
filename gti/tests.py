from django.test import TestCase
from django.test.client import Client

from .models import Category
from .models import Platform
from .models import FrequentQuestion

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


class PlatformTestCase(TestCase):
    def setUp(self):
        Platform.objects.create(platform_name="MOODLE")
        Platform.objects.create(platform_name="SICUA")

    def test_categories_can_speak_get_all(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/platforms/')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 2


class FrequentQuestionsTestCase(TestCase):
    def setUp(self):
        category_one = Category.objects.create(category_name="Examenes")
        category_two = Category.objects.create(category_name="Calificaciones")
        platform_one = Platform.objects.create(platform_name="MOODLE")
        platform_two = Platform.objects.create(platform_name="SICUA")
        FrequentQuestion.objects.create(frequent_questions_name="SICUA", frequent_questions_category=category_one,
                                        frequent_questions_Platform=platform_one)
        FrequentQuestion.objects.create(frequent_questions_name="SICUA", frequent_questions_category=category_two,
                                        frequent_questions_Platform=platform_two)
        FrequentQuestion.objects.create(frequent_questions_name="SICUA", frequent_questions_category=category_one,
                                        frequent_questions_Platform=platform_two)
        FrequentQuestion.objects.create(frequent_questions_name="SICUA", frequent_questions_category=category_two,
                                        frequent_questions_Platform=platform_one)

    def test_frequent_questions_can_speak_get_all(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/frequent_questions/')
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4
