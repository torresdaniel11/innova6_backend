from random import randint

from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from serializers import ArticlesSerializers
from serializers import ConversationsSerializers
from serializers import QuestionsSerializers
from serializers import QuestionArticlesSerializers
from serializers import CategorySerializers
from serializers import QuestionRecordsSerializers

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

    @detail_route(methods=['get'])
    def suggested_questions_get(self, request, *args, **kwargs):
        conversation = self.get_object()
        questions = models.Questions.objects.filter(
            question_conversation_level=conversation.conversation_conversation_level)
        serializer = QuestionsSerializers(questions, many=True)
        i = randint(0, questions.count() - 1)
        return Response(serializer.data[i])

    @detail_route(methods=['post'])
    def save_response_suggested_questions_post(self, request, *args, **kwargs):
        conversation = self.get_object()
        serializer = QuestionRecordsSerializers(data=request.data)
        if serializer.is_valid():
            question = serializer.data['question_record_question']

            conversation_conversation_level = list(models.ConversationLevels.objects.filter(
                id=conversation.conversation_conversation_level.id + 1))

            if conversation_conversation_level:
                conversation.conversation_conversation_level = conversation_conversation_level[0]

            conversation.conversation_name = serializer.data['question_record_response']
            conversation.save()

            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class QuestionView(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    serializer_class = QuestionsSerializers


class QuestionArticlesView(viewsets.ModelViewSet):
    queryset = models.QuestionArticles.objects.all()
    serializer_class = QuestionArticlesSerializers


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializers


class QuestionRecordsView(viewsets.ModelViewSet):
    queryset = models.QuestionRecords.objects.all()
    serializer_class = QuestionRecordsSerializers
