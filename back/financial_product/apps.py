from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

class FinancialProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'financial_product'
    def ready(self):
        from .tasks import my_scheduled_task
        from apscheduler.triggers.cron import CronTrigger
        
        trigger = CronTrigger(hour=11, minute=48)
        scheduler.add_job(my_scheduled_task, trigger)
        scheduler.start()