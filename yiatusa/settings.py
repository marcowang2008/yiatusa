"""
Django settings for yiatusa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9vpb30ibt4(au++!l1h6yjz%!$-7en6j*r5kjf!q9^(dcx5und'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#    'south',
    'home',
    'blog',
    'tinymce',
    'social.apps.django_app.default',
)

SOCIAL_AUTH_FACEBOOK_KEY = '315297042005320'
SOCIAL_AUTH_FACEBOOK_SECRET = '2447f183fb148a3cf594255746617796'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1036597843802-0kkfug1mnrrcruu45n8uec036pib2m06.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'YFLLU83H6rkuI-Mb1cALJD9J'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [...]

SOCIAL_AUTH_TWITTER_KEY = 'lLKfBs6Tzpf2x5c1ilhqVTwOf'
SOCIAL_AUTH_TWITTER_SECRET = 'coXyUEBIQGw0O7lwT6kkorJVESZjrAc3IyP0cXwoYoREsV96Kd'

LOGIN_REDIRECT_URL = '/'

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'yiatusa.urls'

WSGI_APPLICATION = 'yiatusa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'yiatusa',
        'USER': 'yiatusa_app',
        'PASSWORD': 'testtest',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# App-scoped static file path is appname/static/appname/css
STATIC_URL = '/static/'

STATIC_ROOT = '/static/'

# Project-scoped static file path
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "shared"),
    '/var/www/shared/',
)

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'shared'), # Project-scoped shared template files
    os.path.join(BASE_DIR, 'blog', 'templates', 'blog'), # App-specified shared template files
    os.path.join(BASE_DIR, 'home', 'templates', 'home'),
]






