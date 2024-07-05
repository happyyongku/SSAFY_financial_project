from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.contrib.auth import get_user_model
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    try:
        if request.method == 'GET':
            articles = Article.objects.all()
            serializer = ArticleListSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(request.user)
        print(e)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def articles_detail(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
        if request.method == 'GET':
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def comments_list(request, article_pk):
    try:
        article = Article.objects.get(pk=article_pk)
        if request.method == 'GET':
            comments = article.comment_set.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            requested_user = get_user_model().objects.get(pk=request.data['userId'])
            serializer = CommentSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=requested_user, article=article)
                return Response(status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        print('error error')
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_user_article(request, user_pk):
    print('user_article')
    user = get_user_model().objects.get(pk=user_pk)
    articles = user.article_set.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
