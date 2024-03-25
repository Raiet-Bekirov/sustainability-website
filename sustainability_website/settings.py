"""
Django settings for sustainability_website project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9!ehmv$xwnn0lz2-fg557e&lb#=xck-$(3y3+2l1@wxip+$9nw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Disables the browseable API provided by Rest Framework
# Only disable for devlopment and debugging!
# ENABLE FOR DEPLOYMENT

REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
     ),
    
    #'DEFAULT_RENDERER_CLASSES': (
    #    'rest_framework.renderers.JSONRenderer',
    #)

    'DEFAULT_AUTHENTICATION_CLASSES': [
    # Enables DRF built-in token authorisation & authentication
    'rest_framework.authentication.TokenAuthentication',
],
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig', # enables use of django ../api
    'rest_framework', # enable django rest framework
    'frontend', # enables the ../frontend django app
    'rest_framework.authtoken', # enables the built-in DRF token authorisation
    'gamekeeper.apps.GamekeeperConfig', # enables use of django ../api

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sustainability_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sustainability_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DATABASE"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        # 'PORT': os.environ.get("DB_PORT"),
        'URL': os.environ.get("POSTGRES_URL"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'URL': "postgres://default:E6Pnk2SUrOGu@ep-summer-scene-a24098yf-pooler.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require",
#         'PRISMA_URL': "postgres://default:E6Pnk2SUrOGu@ep-summer-scene-a24098yf-pooler.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require&pgbouncer=true&connect_timeout=15",
#         'URL_NO_SSL': "postgres://default:E6Pnk2SUrOGu@ep-summer-scene-a24098yf-pooler.eu-central-1.aws.neon.tech:5432/verceldb",
#         'URL_NON_POOLING': "postgres://default:E6Pnk2SUrOGu@ep-summer-scene-a24098yf.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require",
#         'USER': "default",
#         'HOST': "ep-summer-scene-a24098yf-pooler.eu-central-1.aws.neon.tech",
#         'PASSWORD':"E6Pnk2SUrOGu",
#         'NAME':"welti_go"
#     }
# }


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

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User model for the API app 
AUTH_USER_MODEL = "api.User"

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.0.18', '.vercel.app']

MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'frontend/src/images')


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'frontend/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')