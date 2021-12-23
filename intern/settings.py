"""
Django settings for intern project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from re import L
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# 画像を扱う設定
MEDIA_ROOT = BASE_DIR.joinpath('media')
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oaab#2kr%trbj2h-w9ycf0&f$7dgi2+p=37!cjw$*y0@26pq77'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,

    'loggers':{
        'django':{
            'handlers':['console'],
            'level':'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary':{
            'handlers':['console'],
            'level':'DEBUG',
        },
    },
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev',
        },
    },

    'formatters': {
        'dev': {
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    }
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'myapp',

    'django.contrib.sites',
    'allauth',
    'allauth.account',

    # 'widget_tweaks',
]

# django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
SITE_ID = 1

# これ何やってるかわからん！！！！！allauth.account.auth_backends.AuthenticationBackendって何～～～
AUTHENTICATION_BACKENDS = (
    # 一般ユーザ用(メールアドレス認証)
    'allauth.account.auth_backends.AuthenticationBackend',
    # 管理サイト用(ユーザ名認証)
    'django.contrib.auth.backends.ModelBackend',
)

# メールアドレス認証に変更する設定
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_USERNAME_REQUIRED = True

# サインアップにメールアドレス確認をはさむよう設定
ACCOUNT_EMAIL_VERIFICATION = 'mandatory',
ACCOUNT_EMAIL_REQUIRED = True

# ログアウトリンクのクリック後即ログアウトする設定
ACCOUNT_LOGOUT_ON_GET = True,

# django-allauthが送信するメールの件名に自動付与される接頭辞をブランクにする設定(？)
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''

# ログイン後、ログアウト後にリダイレクトするURLを設定
LOGIN_REDIRECT_URL = "myapp:friends"
LOGOUT_REDIRECT_URL = "index"

# formをカスタマイズ
ACCOUNT_FORMS = {
    'signup': 'myapp.forms.CustomSignUpForm',
}

# ACCOUNT_ADAPTER = 'myapp.adapter.AccoutAdapter'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'intern.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # allauth用です
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'myapp', 'templates', 'account'),
            os.path.join(BASE_DIR, 'myapp'),
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

WSGI_APPLICATION = 'intern.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

'''postgresにすげかえるための設定(なんもわからん)'''
# env = environ.Env()
# env.read_env(os.path.join(BASE_DIR, '.env'))

# DATABASES = {
#    # postgres
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'myapp',
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': '',
#         'PORT': 5433,
#     }
# }
''''''
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTH_USER_MODEL = 'myapp.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

#signupformからの情報をcustomusermodelに保存するのに必要
ACCOUNT_ADAPTER = 'myapp.adapter.AccountAdapter'