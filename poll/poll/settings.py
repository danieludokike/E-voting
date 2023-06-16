from pathlib import Path
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5ax+f5e^7o+f&#*uem@02dg@6btgt%gdp$@b5vk9gr$4$dj#+j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "sterlingpoll.org", "www.sterlingpoll.org", "mail.sterlingpoll.org"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # CLOUDINARY STORAGE
    # 'cloudinary_storage',
    'cloudinary',
    
    # own apps
    "pollapp.apps.PollappConfig",
    "account.apps.AccountConfig",

]

MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
    # ADDING WHITENOISE AND COMMON MIDDLE WARE
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # AUTO LOGOUT MIDDLEWARES
     'django_auto_logout.middleware.auto_logout',
]

# AUTO LOGOUT FUNCTIONALITY
AUTO_LOGOUT = {
            'IDLE_TIME': 200,
            'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
               }


ROOT_URLCONF = 'poll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
            ],
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

WSGI_APPLICATION = 'poll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'outlnfci_base',
#         'USER': 'outlnfci_user',
#         'PASSWORD': 'BnFMnyrfcqrj',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'OPTIONS': {
#             'sql_mode': 'traditional',
#             'charset': 'utf8mb4',
#         }
#     }
#     }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# CLOUDINARY SETTINGS
# adding config
cloudinary.config( 
  cloud_name = "dhfcqnxgn", 
  api_key = "911811297717622", 
  api_secret = "tSu3VBQnpPBBNYxlpUL_JKV_RCQ" 
)


#  EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'server39.web-hosting.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = "support@sterlingpoll.org"
EMAIL_HOST_PASSWORD = "aJD@35^SI__"
DEFAULT_FROM_EMAIL = "support@sterlingpoll.org"
SERVER_EMAIL = "support@sterlingpoll.org"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# # TAWK TO SETTINGS
# TAWKTO_ID_SITE='<tawkto id site>'
# TAWKTO_API_KEY='<tawkto api key>'
# TAWKTO_IS_SECURE=True


if not DEBUG:
    # HTTPs Settings
    SESSION_COOKIE_SECURE = True
    # DJANGO SESSION SETTINGS 
    # sessions
    SESSION_SAVE_EVERY_REQUEST = True
    CSRF_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # HSTS Settings
    SECURE_HSTS_SECONDS = 31536000  # A year
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True


# LOGIN URLS AND REDIRECTIONS
LOGIN_URL ="account:login_view"
LOGIN_REDIRECT_URL = "account:login_view"
LOGOUT_REDIRECT_URL = "account:login_view"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
