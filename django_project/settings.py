
import os
from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY= config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

X_FRAME_OPTIONS = '*'

ALLOWED_HOSTS = ['localhost','192.168.1.5:8000' , '0.0.0.0:8000', '0.0.0.0', '192.168.1.5',
 '127.0.0.1', '192.168.1.8', 'fiberworks-production.up.railway.app','rockymountainknits.com', 'www.rockymountainknits.com',
 'http://www.rockymountainknits.com', 'https://www.rockymountainknits.com']

CSRF_TRUSTED_ORIGINS = [ 'https://fiberworks-production.up.railway.app', 'http://fiberworks-production.up.railway.app',
                          'http://www.rockymountainknits.com', 
                         'https://www.rockymountainknits.com', 'https://rockymountainknits.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fiberworks_app',
    'bootstrap5',
    'storages',
    
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

ROOT_URLCONF = 'django_project.urls'

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
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Jades_Database',
#         'USER': 'JadeDitmanson',
#         'PASSWORD': config('AWS_DATABASE_PASSWORD'),
#         'HOST': 'jadedatabaseid.ci2my4s4bupw.us-east-2.rds.amazonaws.com',  # or the IP address of your PostgreSQL server if it's remote
#         'PORT': '5432',  # default PostgreSQL port
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': config('RAILWAY_DATABASE_PASSWORD'),
        'HOST': 'viaduct.proxy.rlwy.net',  # or the IP address of your PostgreSQL server if it's remote
        'PORT': '59561',  # default PostgreSQL port
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

COVERAGE_RUN_EXTRA_ARGS = [
    '--source=fiberworks_app',  # Replace with the actual name of your app
]

# S3 BUCKETS CONFIGURATION
AWS_ACCESS_KEY_ID = 'AKIA5SKSI47CJIHRG47M'
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'jades-fiberworks-bucket'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"

STATICFILES_STORAGE = 'storages.backends.s3.S3Storage'