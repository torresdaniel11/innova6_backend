from rest_framework import serializers

from .models import Articles
from .models import Category
from .models import ConversationLevels
from .models import Conversations
from .models import QuestionArticles
from .models import QuestionRecords
from .models import Questions


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id', 'article_tittle', 'article_content', 'article_slug', 'article_create_date', 'article_update_date')


class ConversationLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationLevels
        fields = ('id', 'conversation_level_name', 'conversation_color')


class ConversationsSerializers(serializers.HyperlinkedModelSerializer):
    conversation_conversation_level = ConversationLevelsSerializer(many=False)

    class Meta:
        model = Conversations
        fields = (
            'id', 'conversation_token', 'conversation_name', 'conversation_email', 'conversation_platform',
            'conversation_faculty', 'conversation_create_date', 'conversation_update_date',
            'conversation_conversation_level')


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')


class QuestionsSerializers(serializers.HyperlinkedModelSerializer):
    question_conversation_level = ConversationLevelsSerializer(many=False)
    question_category = CategorySerializers(many=False)

    class Meta:
        model = Questions
        fields = (
            'id', 'question_name', 'question_description', 'question_keywords', 'question_conversation_level',
            'question_category', 'question_update', 'question_field_update')


class QuestionArticlesSerializers(serializers.HyperlinkedModelSerializer):
    question_article_question = QuestionsSerializers(many=False)
    question_article_category = CategorySerializers(many=False)

    class Meta:
        model = QuestionArticles
        fields = (
            'id', 'question_article_name', 'question_article_description', 'question_article_keywords',
            'question_article_question', 'question_article_category')


class QuestionRecordsSerializers(serializers.HyperlinkedModelSerializer):
    question_record_conversation = ConversationsSerializers(many=False)
    question_record_question = QuestionsSerializers(many=False)

    class Meta:
        model = QuestionRecords
        fields = (
            'id', 'question_record_response', 'question_record_conversation', 'question_record_question',
            'question_record_token', 'question_record_create_date')
