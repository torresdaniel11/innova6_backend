from random import randint

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from serializers import ArticlesSerializers
from serializers import ConversationsSerializers
from serializers import QuestionsSerializers
from serializers import QuestionArticlesSerializers
from serializers import CategorySerializers
from gti import models


# Create your views here.
class ArticleView(viewsets.ModelViewSet):
    queryset = models.Articles.objects.all()
    serializer_class = ArticlesSerializers


# Create your views here.
class ConversationView(viewsets.ModelViewSet):
    queryset = models.Conversations.objects.all()
    serializer_class = ConversationsSerializers
    lookup_field = 'conversation_token'

    @detail_route()
    def suggested_questions(self, request, *args, **kwargs):
        conversation = self.get_object()
        questions = models.Questions.objects.filter(
            question_conversation_level=conversation.conversation_conversation_level)
        serializer = QuestionsSerializers(questions, many=True)
        i = randint(0, questions.count() - 1)
        return Response(serializer.data[i])

    @detail_route(methods=['post'])
    def suggested_questions(self, request, *args, **kwargs):
        conversation = self.get_object()
        questions = models.Questions.objects.filter(
            question_conversation_level=conversation.conversation_conversation_level)
        serializer = QuestionsSerializers(questions, many=True)
        i = randint(0, questions.count() - 1)
        return Response(serializer.data[i])

    # Create your views here.i]


class QuestionView(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    serializer_class = QuestionsSerializers


class QuestionArticlesView(viewsets.ModelViewSet):
    queryset = models.QuestionArticles.objects.all()
    serializer_class = QuestionArticlesSerializers


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializers
