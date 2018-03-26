from django.shortcuts import render
from rest_framework import viewsets, permissions
from serializers import ArticlesSerialzers
from gti import models


# Create your views here.
class ArticleView(viewsets.ModelViewSet):
    queryset = models.Articles.objects.all()
    serializer_class = ArticlesSerialzers
