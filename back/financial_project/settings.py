"""
Django settings for financial_project project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'article',
    'accounts',
    'stock',
    'financial_product',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_crontab',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

MIDDLEWARE = [
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'financial_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'financial_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DB_PASSWORD = env('DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SSAFY_final',
        'USER': 'yonggu97',
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': 'localhost', # MySQL 호스트
        'PORT': '3306',      # MySQL 포트 (기본값은 3306)
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'


REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.AllowAny'
    ]
    
    
    # 'DEFAULT_AUTHENTICATION_CLASSES':[
    #     'rest_framework.authentication.BasicAuthentication',
    #     'rest_framework.authentication.TokenAuthentication',
    # ],
}

CORS_ALLOWED_ORIGINS= [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
]

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_CAPITAL_REQUIRED = False
# ACCOUNT_

REST_AUTH = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.CustomUserDetailsSerializer',
}

ACCOUNT_ADAPTER = 'accounts.models.CustomAccountAdapter'

API_KEY_EXCHANGE = env('API_KEY_EXCHANGE')
API_KEY_FINANCIAL = env('API_KEY_FINANCIAL')
API_KEY_AI = env('API_KEY_GPT')

# ------------------ apscheduler ------------------------
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
SCHEDULER_DEFAULT=True


#---------------------------------------------------Celery-------------------------------------------------------

# from celery import shared_task
# from celery.schedules import crontab
# from celery import Celery

# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESUTL_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'KST'
# #Asia/Seoul

# app = Celery('financial_project')

# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# CELERY_BEAT_SCHEDULE = {
#     'run-every-morning': {
#         'task': 'financial_product.tasks.my_task',
#         'schedule': crontab(hour=10, minute=15),  # 매일 오전 1시에 실행
#     },
# }
