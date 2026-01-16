"""
Django settings for careerboost_backend project.
"""

from pathlib import Path
import os
import dj_database_url

# ==================================================
# BASE DIRECTORY
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==================================================
# SECURITY
# ==================================================
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError("DJANGO_SECRET_KEY is not set")

DEBUG = False

ALLOWED_HOSTS = [
    "careerboost-backend-production-adad.up.railway.app",
    "localhost",
    "127.0.0.1",
]

# ==================================================
# APPLICATIONS
# ==================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",

    "users",
    "jobs",
]

# ==================================================
# MIDDLEWARE
# ==================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==================================================
# URLS / WSGI
# ==================================================
ROOT_URLCONF = "careerboost_backend.urls"
WSGI_APPLICATION = "careerboost_backend.wsgi.application"

# ==================================================
# TEMPLATES
# ==================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ==================================================
# DATABASE (Railway Postgres)
# ==================================================
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
    )
}

# ==================================================
# PASSWORD VALIDATION
# ==================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==================================================
# INTERNATIONALIZATION
# ==================================================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ==================================================
# STATIC FILES
# ==================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# ==================================================
# CORS
# ==================================================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
CORS_ALLOW_CREDENTIALS = True

# ==================================================
# CSRF / COOKIES (Railway HTTPS)
# ==================================================
CSRF_TRUSTED_ORIGINS = [
    "https://careerboost-backend-production-adad.up.railway.app",
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ==================================================
# PROXY / HTTPS
# ==================================================
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# ==================================================
# REST FRAMEWORK
# ==================================================
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}

# ==================================================
# DEFAULT PK
# ==================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
