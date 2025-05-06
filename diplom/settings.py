from pathlib import Path
from dotenv import load_dotenv
import os


# загружаем .env
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!



# после создания проекта вписываем ключ в env,
#           а строку с secret key меняем на указанную выше
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG")
# включаем/выключаем дебаг в .env
DEBUG = os.getenv("DEBUG")

# вписываем разрешенные деплои
# по умолчанию - 127.0.0.1, при деплое меняем на нужный
ALLOWED_HOSTS = [os.getenv("ALLOWED_HOST"), ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # главное приложение(категории, товары)
    'main',
    # логин, регистрация, выход с профиля
    'users',
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

ROOT_URLCONF = 'diplom.urls'

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

WSGI_APPLICATION = 'diplom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

#Подключаюсь к базе данных Postgres SQL ,после того как создал ее + пользователь
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'diplom'),
        'USER': os.getenv('POSTGRES_USER', 'tsvetkov'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('ALLOWED_HOST'),
        #'127.0.0.1'
        'PORT': os.getenv('POSTGRES_PORT', 5432),
        'ATOMIC_REQUESTS': True,
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# по умолчанию ру язык, мск время, при желании - меняем в .env
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', 'ru-RU')
TIME_ZONE = os.getenv('TIME_ZONE', 'Europe/Kiev')


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# для работы фотографий на сайте(НЕ относится к статическим изображениям)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# для работы users
AUTH_USER_MODEL = 'users.User'
