from django.urls import path, include
from . import views

urlpatterns = [
    path('get_data/', views.get_data)
]