# Django settings base project.
from decouple import config, Csv
from pathlib import Path
from dj_database_url import parse as db_url
from datetime import timedelta

# snippet for django-fernet-fields on django 4
# https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding
import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
# end of snippet


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-CH'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static'

# Static files (CSS, JavaScript, Images)
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_URL = 'static/'

# Additional locations of static files
STATICFILES_DIRS = (
    str(BASE_DIR / 'core/users/static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'django_ilus_skeleton/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # django-auto-logout
                'django_auto_logout.context_processors.auto_logout_client',
            ],
        },
    },
]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware', replaced with below
    'user_sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # django-two-factor-auth (place after AuthenticationMiddleware)
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pwned_passwords_django.middleware.PwnedPasswordsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',

    # django-auto-logout
    # append after default middlewares
    'django_auto_logout.middleware.auto_logout',


    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'django_ilus_skeleton.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'django_ilus_skeleton.wsgi.application'

# django-axes
AXES_FAILURE_LIMIT = 10
AXES_COOLOFF_TIME = timedelta(minutes=10)
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True
AXES_LOCKOUT_TEMPLATE = 'core/user/lockout.html'

# django-two-factor-auth
TWO_FACTOR_PATCH_ADMIN = True
TWO_FACTOR_LOGIN_TIMEOUT = 600
PHONENUMBER_DEFAULT_REGION = 'CH'
LOGIN_URL = 'two_factor:login'
LOGIN_REDIRECT_URL = 'two_factor:profile'
LOGOUT_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'users.CustomUser'

# django-auto-logout
from datetime import timedelta

AUTO_LOGOUT = {
    'IDLE_TIME': timedelta(minutes=20),
    'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
    'SESSION_TIME': timedelta(hours=1),
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# Application definition

INSTALLED_APPS = [
    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    # 'django.contrib.sessions', # replaced with below
    # django-user-sessions
    'user_sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',

    # ##################################
    # External plugins

    #
    'django_auto_logout',

    # django-two-factor-auth
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'otp_yubikey',
    'two_factor',

    # django-axes
    'axes',

    # django-bootstrap-v5
    'bootstrap5',

    # django-simple-menu
    'menu',

    # django-robots
    'robots',

    # local apps
    'core.users',
    'apps.pages',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'pwned_passwords_django.validators.PwnedPasswordsValidator',
        'OPTIONS': {
            'error_message': 'That password was pwned',
            'help_message': 'Your password can\'t be a commonly used password.',
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 15}
    },
    {
        'NAME': 'core.users.validators.ConsecutivelyRepeatingCharacterValidator',
        'OPTION': {'length': 3}
    },
    {
        'NAME': 'core.users.validators.ConsecutivelyIncreasingIntegerValidator',
        'OPTION': {'length': 3}
    },
    {
        'NAME': 'core.users.validators.ConsecutivelyDecreasingIntegerValidator',
        'OPTION': {'length': 3}
    },
    {
        'NAME': 'core.users.validators.UppercaseValidator',
    },
    {
        'NAME': 'core.users.validators.LowercaseValidator',
    },
    {
        'NAME': 'core.users.validators.SymbolValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'core.users.validators.ContextValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.ScryptPasswordHasher',
]

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

FERNET_KEYS = [
    'django-insecure-2-hgml%)xg2=zya3e3+wkto+(yp!^0+g)0!v#e*l5eby!h3tp#',
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = config('TEMPLATE_DEBUG', default=False, cast=bool)

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        cast=db_url
    )
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# django-user-sessions https://github.com/jazzband/django-user-sessions
SESSION_ENGINE = 'user_sessions.backends.db'
SILENCED_SYSTEM_CHECKS = ['admin.E410', ]

# django-simple-menu https://github.com/jazzband/django-simple-menu
MENU_SELECT_PARENTS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
