
from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.articles_detail),
    path('articles/user/<int:user_pk>/', views.get_user_article),
    path('articles/<int:article_pk>/comments/', views.comments_list),
]