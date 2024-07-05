
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django의 settings 모듈을 Celery의 기본 모듈로 설정합니다.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'financial_project.settings')

app = Celery('financial_project')

# 여기서 문자열을 사용하는 이유는 작업자를 위한 이름으로 생성된 객체가 
# 직렬화될 때 문제가 발생하지 않도록 하기 위해서입니다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Django의 모든 등록된 앱 구성에서 task 모듈을 로드합니다.
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))