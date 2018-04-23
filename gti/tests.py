from django.test import TestCase
from django.test.client import Client

from .models import Category
from .models import Platform
from .models import FrequentQuestion
from .models import Conversations
from .models import ConversationLevels
from .models import QuestionRecords
from .models import Questions
from .models import TypeArticle
from .models import Articles

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

    def test_categories_can_speak_get_by_id(self):
        client = Client()
        response = client.get('http://127.0.0.1:8000/categories/1/')
        assert response.status_code == 200


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


class RetrieveConversationsID(TestCase):
    def setUp(self):
        conversation_level_qualification = ConversationLevels.objects.create(id=3,
                                                                             conversation_level_name="Seleccionar categoria",
                                                                             conversation_color="BLUE")
        Conversations.objects.create(
            id=1,
            conversation_token='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
            conversation_name='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
            conversation_email="fg.captuayo@uniandes.edu.co",
            conversation_platform="SICUA",
            conversation_faculty="N/A",
            conversation_conversation_level=conversation_level_qualification,
        )

    def test_frequent_questions_can_speak_get_all_by_category_plataform(self):
        client = Client()
        response = client.get(
            'http://127.0.0.1:8000/conversations/e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23/')
        assert response.status_code == 200


class RetrieveRecordsConversationsID(TestCase):
    def setUp(self):
        conversation_level_qualification = ConversationLevels.objects.create(id=3,
                                                                             conversation_level_name="Seleccionar categoria",
                                                                             conversation_color="BLUE")

        category_two = Category.objects.create(category_name="Calificaciones")

        question_qualification = Questions.objects.create(question_name="Pregunta de califiacion",
                                                          question_description="calificacion",
                                                          question_keywords="calificacion",
                                                          question_conversation_level=conversation_level_qualification,
                                                          question_category=category_two
                                                          )

        conversation = Conversations.objects.create(
            id=1,
            conversation_token='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
            conversation_name='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
            conversation_email="fg.captuayo@uniandes.edu.co",
            conversation_platform="SICUA",
            conversation_faculty="N/A",
            conversation_conversation_level=conversation_level_qualification,
        )

        QuestionRecords.objects.create(question_record_response="Calificaciones",
                                       question_record_conversation=conversation,
                                       question_record_question=question_qualification,
                                       question_record_token='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
                                       )

    def test_frequent_questions_can_speak_get_all_by_category_plataform(self):
        client = Client()
        response = client.get(
            'http://127.0.0.1:8000/retrieve_frequency_questions/e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23/')
        assert response.status_code == 200


class RetrieveArticlesByTokenConversation(TestCase):
    def setUp(self):
        conversation_level_qualification = ConversationLevels.objects.create(id=3,
                                                                             conversation_level_name="Seleccionar categoria",
                                                                             conversation_color="BLUE")

        category_two = Category.objects.create(category_name="Calificaciones")

        question_qualification = Questions.objects.create(question_name="Pregunta de califiacion",
                                                          question_description="calificacion",
                                                          question_keywords="calificacion",
                                                          question_conversation_level=conversation_level_qualification,
                                                          question_category=category_two
                                                          )

        conversation = Conversations.objects.create(
            id=1,
            conversation_token='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
            conversation_name='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
            conversation_email="fg.captuayo@uniandes.edu.co",
            conversation_platform="SICUA",
            conversation_faculty="N/A",
            conversation_conversation_level=conversation_level_qualification,
        )

        QuestionRecords.objects.create(question_record_response="Calificaciones",
                                       question_record_conversation=conversation,
                                       question_record_question=question_qualification,
                                       question_record_token='e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23',
                                       )

        typeArticule = TypeArticle.objects.create(platform_name="INTERNO")


        Articles.objects.create(article_tittle="Calificaciones",
                                article_content="Calificaciones",
                                article_slug="Calificaciones",
                                question_category=category_two,
                                article_url="n/a",
                                article_type_article=typeArticule)


        def test_frequent_questions_can_speak_get_all_by_category_plataform(self):
            client = Client()
            response = client.get(
                'http://127.0.0.1:8000/retrieve_article/e684c238be3c8318571435637814afb394985b2625de2cff888f0fa68c23/')
            assert response.status_code == 200

    class TypeArticleTestCase(TestCase):
        def setUp(self):
            TypeArticle.objects.create(platform_name="INTERNO")
            TypeArticle.objects.create(platform_name="PDF")
            TypeArticle.objects.create(platform_name="YOUTUBE")
            TypeArticle.objects.create(platform_name="PAGINA WEB")

        def test_categories_can_speak_get_all(self):
            client = Client()
            response = client.get('http://127.0.0.1:8000/type_articles/')
            assert response.status_code == 200
            assert len(json.loads(response.content)) == 4
