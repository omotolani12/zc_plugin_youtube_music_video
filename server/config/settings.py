import os
from pathlib import Path

import environ  # import environ

env = environ.Env()  # Initialise environment variables
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Declared in your environment variables
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["zuri.chat", "music.zuri.chat", "159.65.123.65", "localhost", "127.0.0.1", "*"]

# Application definition
CORS_ALLOW_ALL_ORIGINS = True

CORS_REPLACE_HTTPS_REFERER = True

INSTALLED_APPS = [
    "corsheaders",  # To Connect API with React App if required in seprate apps
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "music",
    "client",
    "rest_framework",  # https://www.django-rest-framework.org/
    "rest_framework.authtoken",
    "allauth",  # https://django-allauth.readthedocs.io/en/latest/installation.html
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "django_extensions",
    "drf_spectacular",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # new
    "django.middleware.common.CommonMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "159.65.123.65",
    # ...
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [
            os.path.join(BASE_DIR, '../root/dist'),
        ],  # Django look for templates folder in root directory
        "APP_DIRS": True,  # Django look for templates folder in app directory
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Create a file named .env and Declare your environment variables for database in .env
# Make sure you don’t use quotations around strings.
DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASS"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = str(BASE_DIR.joinpath("staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../root/dist'),
    os.path.join(BASE_DIR, 'client/dist'),
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = "./media"
MEDIA_URL = "/media/"
# Fixtures
FIXTURE_DIRS = ["fixtures"]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Auth user
# Configure django-rest-framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    # "DEFAULT_RENDERER_CLASSES": [
    #     "rest_framework.renderers.JSONRenderer",
    # ],
    # "DEFAULT_PARSER_CLASSES": [
    #     "rest_framework.parsers.JSONParser",
    # ],
    # "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'YouTube Music Plugin API',
    'DESCRIPTION': 'YouTube Music Plugin for Zuri.Chat',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}

# For django.contrib.sites
SITE_ID = 1

# Configure django-allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = None
ACCOUNT_UNIQUE_EMAIL = True

# Allow entering as a guest
ALLOW_GUEST_ACCESS = bool(os.environ.get("DJANGO_ALLOW_GUEST_ACCESS", default=""))


#CORS_ALLOWED_ORIGINS = [
    
 #   "https://sub.example.com",
  #  "http://localhost:8080",
   # "http://localhost:8000",
    #"http://localhost:9000",
    #"http://localhost:3000",  # if you have seprate react app
#]

if bool(os.environ.get("PRODUCTION_SERVER", default="")):
    SECURE_SSL_REDIRECT = True

ORGANIZATON_ID = "614679ee1a5607b13c00bcb7"  # given by mark.
PLUGIN_ID = "613ceb50ceee2ab59d44df2f"
CENTRIFUGO_TOKEN = "58c2400b-831d-411d-8fe8-31b6e337738b"

# new collections created
ROOM_COLLECTION = "music_room"
SONG_COLLECTION = "songs"
COMMENTS_COLLECTION = "chats"
MEMBERS_COLLECTION = "room_users"

APPEND_SLASH = False
