from rest_framework import serializers
from .models import Articles
from .models import Conversations


class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = (
            'id', 'article_tittle', 'article_content', 'article_slug', 'article_create_date', 'article_update_date')


class ConversationsSerializers(serializers.HyperlinkedModelSerializer):
    conversation_token = serializers.SerializerMethodField('conversation_token')

    def get_thumbnail_url(self, obj):
        return '%s%s' % (settings.MEDIA_URL, obj.thumbnail)

    class Meta:
        model = Conversations
        fields = (
            'id', 'conversation_token', 'conversation_name', 'conversation_email', 'conversation_platform',
            'conversation_faculty', 'conversation_create_date', 'conversation_update_date',
            'conversation_conversation_level')
