from rest_framework import serializers
from .models import Articles
from .models import Conversations


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
