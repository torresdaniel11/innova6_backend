from os import link

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from serializers import ArticlesSerializers
from serializers import ConversationsSerializers
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

