from rest_framework import serializers
from .models import Articles

class ArticlesSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'article_tittle', 'article_content', 'article_slug', 'article_create_date', 'article_update_date')