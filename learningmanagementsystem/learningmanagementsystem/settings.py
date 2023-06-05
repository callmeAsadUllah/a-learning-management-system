from pathlib import Path
# from django.core.management.commands.runserver import Command as runserver

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-w99+u+#$jwz#g!hss0k1w0+19oe2pcl*)xu*3u*-8g4a^nd=85'

AUTH_USER_MODEL = 'userapp.MyUser'

LOGIN_URL = ''

LOGIN_REDIRECT_URL = ''

LOGOUT_URL = ''

LOGOUT_REDIRECT_URL = ''

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

# runserver.default_port = ''

# runserver.default_addr = 'localhost'

# runserver.default_addr = '127.0.0.1'

INSTALLED_APPS = [
    #
    'testapp',
    #
    'userapp',
    #
    'courseapp',
    #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'django.contrib.sites',
    #
    'django.contrib.postgres',
    #
    'django_extensions',
    #
    'rest_framework'
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

ROOT_URLCONF = 'learningmanagementsystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
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

WSGI_APPLICATION = 'learningmanagementsystem.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alms',
        'USER': 'alms',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5435'
    }
}

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

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ]
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
