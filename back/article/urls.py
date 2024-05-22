
from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.articles_detail),
    path('articles/<int:article_id>/comments/', views.comments_list),
]