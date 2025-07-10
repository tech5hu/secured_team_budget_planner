from pathlib import Path
import os
from dotenv import load_dotenv

# load variables from.env to os.environ
load_dotenv()

# base directory for the project (used to build paths)
BASE_DIR = Path(__file__).resolve().parent.parent

# secret key
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-fallback-key')

# enable debug mode only for development, not live environments, optional
# dynamic support
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# list of allowed domains (empty means localhost only), with optional
# future support
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# installed apps — includes default django apps and our custom ones
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'budgets',  # custom app for budget tracking
    'users',    # custom app for user auth/registration
]

# middleware handles requests/responses across the app
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # protects against csrf attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# main url config for the app
ROOT_URLCONF = 'team_budget_planner.urls'

# template configuration for rendering HTML pages
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # custom templates folder
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

# entry point for running the app
WSGI_APPLICATION = 'team_budget_planner.wsgi.application'

# using sqlite3 database (default for small apps and development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# password validators help ensure strong user passwords
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

# set default language and time zone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# static file (css/js) settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # folder where custom CSS/JS lives
]
# folder for collected static files (eg for deployment)
STATIC_ROOT = BASE_DIR / "staticfiles"

# default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# login/logout redirects
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/users/login/'
