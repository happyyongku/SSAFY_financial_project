
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from datetime import date
from .models import ExchangRate
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

def my_scheduled_task():
    url = 'http://127.0.0.1:8000/financial_product/get_exchange_data/2024-04-01/'
    response = requests.post(url)
    print(response)
    return Response(status=status.HTTP_201_CREATED)