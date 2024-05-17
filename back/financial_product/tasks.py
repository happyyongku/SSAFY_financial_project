from celery import shared_task
from datetime import datetime

@shared_task
def get_data():
    ...