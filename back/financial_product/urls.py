from django.urls import path, include
from . import views

urlpatterns = [
    path('get_financial_data/', views.get_financial_data),
    path('check/', views.check_data),
    path('get_exchange_data/', views.get_exchange_data),
    path('search/', views.search)
]