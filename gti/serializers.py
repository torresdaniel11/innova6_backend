from rest_framework import serializers
from .models import Articles
from .models import Conversations
from .models import Questions
from .models import QuestionArticles
from .models import QuestionRecords


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id', 'article_tittle', 'article_content', 'article_slug', 'article_create_date', 'article_update_date')


class ConversationsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversations
        fields = (
            'id', 'conversation_token', 'conversation_name', 'conversation_email', 'conversation_platform',
            'conversation_faculty', 'conversation_create_date', 'conversation_update_date')


class QuestionsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = (
            'id', 'question_name', 'question_description', 'question_keywords')


class QuestionArticlesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionArticles
        fields = (
            'id', 'question_article_name', 'question_article_description', 'question_article_keywords')


class QuestionRecordsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionRecords
        fields = (
            'id', 'question_record_create_date', 'question_record_response')
