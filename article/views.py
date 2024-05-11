from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article, Comment
from .serializers import ArticleListSerializer
# Create your views here.

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
