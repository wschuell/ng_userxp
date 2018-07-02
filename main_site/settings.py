"""
Django settings for main_site project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '66*1bsp6-cpqvibx&dpnru)h5v_hk^t)y9(z7a&2ohv=uxs=y*'
from .secretkey import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
if os.path.isfile("debug.txt"):
    with open("debug.txt",'r') as f:
        DEBUG = json.loads(f.read())
else:
    DEBUG = True
    with open("debug.txt",'w') as f:
        f.write(json.dumps(DEBUG))

#ALLOWED_HOSTS = ['192.168.43.57','127.0.0.1','10.15.0.1']
if os.path.isfile("allowed_hosts.txt"):
    with open("allowed_hosts.txt",'r') as f:
        ALLOWED_HOSTS = json.loads(f.read())
else:
    ALLOWED_HOSTS = ['0.0.0.0']
    with open("allowed_hosts.txt",'w') as f:
        f.write(json.dumps(ALLOWED_HOSTS))

# Application definition

INSTALLED_APPS = [
    'ng.apps.NgConfig',
    'django.contrib.admin',
    #'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_admin_generator',

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

ROOT_URLCONF = 'main_site.urls'

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

WSGI_APPLICATION = 'main_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #},

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ng_userxp',
        'USER': 'ng_userxp_user',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '',
        #'TEST':{
        #    'ENGINE': 'django.db.backends.sqlite3',
        #    'NAME': os.path.join(BASE_DIR, 'test_ng_userxp_db.sqlite3'),
        #    },
    }

}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Rome' #'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
