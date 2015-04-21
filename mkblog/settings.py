"""
Django settings for mkblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1#lm$5e5k-+oe@3grcc9_2m6o5+bfy=1jmpnv^cc-@*i1awl4i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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
    'django_crontab',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.VisitorMiddleWare'
)

ROOT_URLCONF = 'mkblog.urls'

WSGI_APPLICATION = 'mkblog.wsgi.application'

TIME_ZONE='Asia/Shanghai'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mkblog',
        'USER': 'blog',
        'PASSWORD': 'qwe123',
        'HOST': 'moka20477.mysql.rds.aliyuncs.com',
        'POST': '3306'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = ''

STATICFILES_DIRS = (os.path.join('static'), )

STATIC_URL = '/static/'

LOGGING = {
'version': 1,
'disable_existing_loggers': False,
'filters': {
    'require_debug_false': {
        '()': 'django.utils.log.RequireDebugFalse'
    },
    'require_debug_true': {
        '()': 'django.utils.log.RequireDebugTrue'
    },
},
'handlers': {
    'mail_admins': {
        'level': 'ERROR',
        'filters': ['require_debug_false'],
        'class': 'django.utils.log.AdminEmailHandler'
    },
    'debug_console': {
        'level': 'DEBUG',
        'filters': ['require_debug_true'],
        'class': 'logging.StreamHandler'
    },
},
'loggers': {
    'django.request': {
        'handlers': ['mail_admins'],
        'level': 'ERROR',
        'propagate': True,
    },
    'django_crontab.crontab': {
    'handlers': ['debug_console'],
    'level': 'WARNING',
    'propagate': False,
    },
}
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

CRONJOBS = [
    ('*/1 * * * *', 'blog.utils.rss_subscribe'),
]

