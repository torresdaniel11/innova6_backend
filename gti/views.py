import random
import operator
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from serializers import ArticlesSerializers
from serializers import ConversationsSerializers
from serializers import QuestionsSerializers
from serializers import QuestionArticlesSerializers
from serializers import CategorySerializers
from serializers import QuestionRecordsSerializers
from serializers import ConversationLevelsSerializer
from serializers import EvaluateConversationSerializers
from serializers import PlatformSerializers
from serializers import FrequentQuestionSerializers
from serializers import TypeArticleSerializers
from serializers import ConfigSerializers
from serializers import TypeUserSerializers

from .models import QuestionRecords

from rest_framework.parsers import JSONParser

from gti import models


class ArticleView(viewsets.ModelViewSet):
    queryset = models.Articles.objects.all()
    serializer_class = ArticlesSerializers


class ConversationView(viewsets.ModelViewSet):
    queryset = models.Conversations.objects.all()
    serializer_class = ConversationsSerializers
    lookup_field = 'conversation_token'

    @detail_route(methods=['get'])
    def suggested_questions_get(self, request, *args, **kwargs):
        conversation = self.get_object()
        questions = models.Questions.objects.filter(
            question_conversation_level=conversation.conversation_conversation_level)

        if questions.count():
            serializer = QuestionsSerializers(questions, many=True)
            max = questions.count() - 1
            i = random.randint(0, max)
            return Response(serializer.data[i])
        else:
            return Response(status=status.HTTP_200_OK)

    @detail_route(methods=['post'])
    def save_response_suggested_questions_post(self, request, *args, **kwargs):
        conversation = self.get_object()

        data = JSONParser().parse(request)
        serializer = QuestionRecordsSerializers(data=data)

        conversation_conversation_level = list(models.ConversationLevels.objects.filter(
            id=conversation.conversation_conversation_level.id + 1))

        if serializer.is_valid():
            question = models.Questions.objects.get(
                id=serializer.initial_data.get('question_record_question', None).get('id'))

            conversation_conversation_level = list(models.ConversationLevels.objects.filter(
                id=conversation.conversation_conversation_level.id + 1))

            if conversation_conversation_level:
                conversation.conversation_conversation_level = conversation_conversation_level[0]

            if question.question_update:
                if question.question_field_update == 'conversation_name':
                    conversation.conversation_name = serializer.data['question_record_response']
                elif question.question_field_update == 'conversation_email':
                    conversation.conversation_email = serializer.data['question_record_response']
                elif question.question_field_update == 'conversation_platform':
                    conversation.conversation_platform = serializer.data['question_record_response']
                elif question.conversation_platform == 'conversation_faculty':
                    conversation.conversation_faculty = serializer.data['question_record_response']

            conversation.save()

            qr = QuestionRecords(question_record_response=serializer.data['question_record_response'],
                                 question_record_conversation=conversation,
                                 question_record_question=question,
                                 question_record_token=conversation.conversation_token)
            qr.save()

            conversationr_response = models.Conversations.objects.get(
                conversation_token=conversation.conversation_token)
            return Response(ConversationsSerializers(conversationr_response).data)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['get'])
    def retrieve_response_suggested_questions_post(self, request, *args, **kwargs):
        conversation = self.get_object()
        questions = models.QuestionRecords.objects.filter(
            question_record_token=conversation.conversation_token)
        serializer = QuestionRecordsSerializers(questions, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def retrieve_frequency_questions_get(self, request, *args, **kwargs):
        nameCategory = None
        conversation = self.get_object()

        questionRecords = models.QuestionRecords.objects.filter(
            question_record_token=conversation.conversation_token)

        for questionRecord in questionRecords:
            if (questionRecord.question_record_question.question_conversation_level.id == 4):
                nameCategory = questionRecord.question_record_response
                break

        category = models.Category.objects.filter(category_name=nameCategory)
        questionRecords = list(models.FrequentQuestion.objects.filter(
            frequent_questions_category=category))
        serializer = FrequentQuestionSerializers(questionRecords, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def retrieve_article_get(self, request, *args, **kwargs):
        nameCategory = None
        conversation = self.get_object()

        questionRecords = models.QuestionRecords.objects.filter(
            question_record_token=conversation.conversation_token)

        for questionRecord in questionRecords:
            if (questionRecord.question_record_question.question_conversation_level.id == 4):
                nameCategory = questionRecord.question_record_response
                break

        category = models.Category.objects.filter(category_name=nameCategory)
        questionRecords = list(models.Articles.objects.filter(
            question_category=category))
        serializer = ArticlesSerializers(questionRecords, many=True)
        return Response(serializer.data)

    @detail_route(methods=['get'])
    def retrieve_suggestion_questions_get(self, request, *args, **kwargs):
        namePlataform = None
        conversation = self.get_object()

        questionRecords = models.QuestionRecords.objects.filter(
            question_record_token=conversation.conversation_token)

        for questionRecord in questionRecords:
            if (questionRecord.question_record_question.question_conversation_level.id == 5):
                namePlataform = questionRecord.question_record_response
                break

        plataform = models.Platform.objects.filter(category_name=namePlataform)
        questionRecords = list(models.FrequentQuestion.objects.filter(
            frequent_questions_Platform=plataform))
        serializer = FrequentQuestionSerializers(questionRecords, many=True)
        return Response(serializer.data)


class QuestionView(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    serializer_class = QuestionsSerializers


class QuestionArticlesView(viewsets.ModelViewSet):
    queryset = models.QuestionArticles.objects.all()
    serializer_class = QuestionArticlesSerializers


class ConversationLevelsView(viewsets.ModelViewSet):
    queryset = models.ConversationLevels.objects.all()
    serializer_class = ConversationLevelsSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializers


class QuestionRecordsView(viewsets.ModelViewSet):
    queryset = models.QuestionRecords.objects.all()
    serializer_class = QuestionRecordsSerializers


class EvaluateConversationView(viewsets.ModelViewSet):
    queryset = models.EvaluateConversation.objects.all()
    serializer_class = EvaluateConversationSerializers


class PlatformView(viewsets.ModelViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = PlatformSerializers


class FrequentQuestionView(viewsets.ModelViewSet):
    queryset = models.FrequentQuestion.objects.all()
    serializer_class = FrequentQuestionSerializers


class TypeArticleView(viewsets.ModelViewSet):
    queryset = models.TypeArticle.objects.all()
    serializer_class = TypeArticleSerializers


class ConfigView(viewsets.ModelViewSet):
    queryset = models.Config.objects.all()
    serializer_class = ConfigSerializers


class TypeUserView(viewsets.ModelViewSet):
    queryset = models.TypeUser.objects.all()
    serializer_class = TypeUserSerializers
