"""
Django settings for abbysapi project.

Generated by 'django-admin startproject' using Django 2.2.27.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""


import os
import sys
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append("/home/nmbajah/AbbysAPI/abbysapi/abbysapi")



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u7edsgx38-im+mpp_p7df4h+ck*-wb1jnsg5l#9rnyc-k5&vxe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
	'rest_framework.authtoken',
    'corsheaders',
    'authemail',
	'accounts',
    'forum',
    'private_messages',
    'django_filters',
]

AUTH_USER_MODEL = 'accounts.MyUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

CORS_ALLOWED_ORIGINS = [
    "http://192.168.190.100:8080",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "https://abby-seven.vercel.app",
   
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://192.168.190.100:8080",
    "http://localhost:8081",
    "https://abby-seven.vercel.app",
    
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


ROOT_URLCONF = 'abbysapi.urls'
AUTH_EMAIL_VERIFICATION = False

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.TokenAuthentication',
	)
}

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

WSGI_APPLICATION = 'abbysapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'abbydb',
#         'USER': 'root',
#         'PASSWORD': 'Starten1@',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

DEFAULT_FROM_EMAIL = "mambo@iqsacco.com"

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_FROM = os.environ.get('EMAIL_FROM') 
# EMAIL_BCC = os.environ.get('EMAIL_BCC')

# EMAIL_HOST = os.environ.get('EMAIL_HOST') 
# EMAIL_PORT = os.environ.get('EMAIL_PORT') 
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') 
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "nmbajah@gmail.com"
EMAIL_HOST_PASSWORD = 'fwliangggleosuha'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


SITE_URL = 'http://localhost:8080/signup/verify/?code='




