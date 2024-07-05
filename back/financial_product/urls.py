from django.urls import path, include
from . import views

urlpatterns = [
    path('get_financial_data/', views.get_financial_data),
    path('check/', views.check_data),
    path('get_exchange_data/', views.get_exchange_data),
    path('get_exchange_data/<str:start_date>/', views.get_exchange_term_data),
    path('get_rate/<str:date>/', views.get_rate),
    path('search/bank_list/', views.get_bank_list),
    path('search/product/<str:type>/<int:bank_id>/', views.get_product_list),
    path('search/option/<str:type>/<int:product_id>/', views.get_option_list),
    path('fetch/product/<str:type>/', views.fetch_product),
    path('fetch/exchange/', views.fetch_exchange),
    path('fetch/exchange/<str:unit>/', views.fetch_exchange_unit),
    path('chat/', views.chatAI),
    path('chat/initialize/', views.history_initialize),
    path('read_product/<str:type>/', views.read_product)
]