<<<<<<< HEAD:pi1t7g18/settings/base.py
=======
"""
Django settings for pi1tg18 project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import sys

>>>>>>> 16093fb (created app schedule, config and tests):pi1tg18/settings/base.py
from environ import Env
from pathlib import Path

from django.contrib.messages import constants

env = Env(
    DEBUG=(bool, False),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env.read_env(
    BASE_DIR / '.env'
)

<<<<<<< HEAD:pi1t7g18/settings/base.py
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

=======
FULLCALENDAR_FOLDER = (BASE_DIR / 'django-fullcalendar')

if FULLCALENDAR_FOLDER not in sys.path:
    sys.path.insert(0, FULLCALENDAR_FOLDER)

# Uncomment below to customize django-fullcalendar settings

# FULLCALENDAR = {
#     'css_url': '',
#     'javascript_url': '',
#     'jquery_url': '',
#     'jquery_ui_url': '',
# }
>>>>>>> 16093fb (created app schedule, config and tests):pi1tg18/settings/base.py

# Application definition

INSTALLED_APPS = [
    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
<<<<<<< HEAD:pi1t7g18/settings/base.py
    # 3td APPS
=======
    # 3td apps
>>>>>>> 70b58ba (add app school and config pages):pi1tg18/settings/base.py
    'allauth',
    'allauth.account',
<<<<<<< HEAD:pi1t7g18/settings/base.py
    # MY APPS
    'core',
    'school',
    'graduation',
    'teacher',
    'group',
=======
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
<<<<<<< HEAD:pi1t7g18/settings/base.py
>>>>>>> 16093fb (created app schedule, config and tests):pi1tg18/settings/base.py
=======
    # My Apps
    'core',
>>>>>>> 70b58ba (add app school and config pages):pi1tg18/settings/base.py
    'schedule',
    'school',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'pi1t7g18.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'pi1t7g18.wsgi.application'


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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

DECIMAL_SEPARATOR = ','

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'templates/static/'
]
STATIC_ROOT = BASE_DIR / 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MESSAGE TAGS

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-dark',
    constants.ERROR: 'alert-danger',
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
}

# Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

LOGIN_URL = 'accounts/login'
LOGOUT_URL = 'accounts/logout'

# Configuração para página não encontrada (404)
handler404 = 'core.views.page_not_found'
# Configuração para erro interno do servidor (500)
handler500 = 'core.views.server_error'