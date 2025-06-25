from pathlib import Path

# base directory for the project (used to build paths)
BASE_DIR = Path(__file__).resolve().parent.parent

# enable debug mode only for development, not live environments
DEBUG = True

# list of allowed domains (empty means localhost only)
ALLOWED_HOSTS = []

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
STATIC_ROOT = BASE_DIR / "staticfiles"  # folder for collected static files (eg for deployment)

# default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# login/logout redirects
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/users/login/'
