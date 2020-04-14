"""
Django settings for config project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
import logging
import logging.config
from configurations import Configuration, values


class Common(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = values.SecretValue()

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'whitenoise.runserver_nostatic',
        'django.contrib.staticfiles',

        'django_extensions',
        
        'wagtail.core',
        'wagtail.admin',
        'wagtail.documents',
        'wagtail.snippets',
        'wagtail.users',
        'wagtail.images',
        'wagtail.embeds',
        'wagtail.search',
        'wagtail.sites',
        'wagtail.contrib.redirects',
        'wagtail.contrib.forms',
        'wagtail.contrib.sitemaps',
        'wagtail.contrib.routable_page',
        'taggit',
        'modelcluster',
        'django_social_share',
        'puputcodeblock',
        'wagtailcodeblock',
        'puput',

        'config.users',
    ]

    MIDDLEWARE = [
        # 'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'wagtail.core.middleware.SiteMiddleware',
        'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    ]

    ROOT_URLCONF = 'config.urls'

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
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'config.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    )

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/2.2/topics/i18n/
    # LANGUAGE_CODE = 'en-us'
    LANGUAGE_CODE = 'zh-hans'

    LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'), ]

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    ]

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

    AUTH_USER_MODEL = 'users.User'

    PUPUT_ENTRY_MODEL = 'puputcodeblock.models.EntryAbstract'

    
    WAGTAIL_SITE_NAME = 'Dev Blog'
    WAGTAIL_CODE_BLOCK_THEME = 'coy'
    WAGTAIL_CODE_BLOCK_LANGUAGES = (
            ('bash', 'Bash/Shell'),
            ('css', 'CSS'),
            ('diff', 'diff'),
            ('html', 'HTML'),
            ('javascript', 'Javascript'),
            ('json', 'JSON'),
            ('python', 'Python'),
            ('scss', 'SCSS'),
            ('yaml', 'YAML'),
        )

    CACHES = {
            "default": {
                "BACKEND": "django.core.cache.backends.db.DatabaseCache",
                "LOCATION": "database_cache",
            }
        }

    # Reset logging
    LOGFILE_ROOT = os.path.join(BASE_DIR, 'logs')
    # (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)

    # Reset logging
    LOGGING_CONFIG = None
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', ],
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse'
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s.%(funcName)s: %(message)s'
            },
            'simple': {
                'format': '%(levelname)s: %(module)s - %(message)s'
            },
        },
        'handlers': {
            # 'null': {
            #     'level': 'DEBUG',
            #     'class': 'django.utils.log.NullHandler',
            # },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false', ],
                'class': 'django.utils.log.AdminEmailHandler'
            },
            'log': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'web.log'), 
                'maxBytes': 1024*1024*5,  # 5 MB
                'backupCount': 5,
                'formatter': 'verbose',
            },
            'log_warning': {
                'level': 'WARNING',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'errors.log'),
                'maxBytes': 1024*1024*5,  # 5 MB
                'backupCount': 5,
                'formatter': 'verbose',
            },
            'request_log': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'web-request.log'),
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter': 'verbose',
            },
        },
        'loggers': {
            '': {
                'handlers': ['console', 'log_warning'],
                'level': 'INFO', #  or 'DEBUG'
            },
            'django.db.backends': {
                'handlers': ['console', ],
                'level': 'ERROR',
                'propagate': False,
            },
            'django': {
                'handlers': ['log', 'log_warning'],
                'propagate': True,
                'level': 'INFO',
            },
            'app': {
                'handlers': ['log_warning', 'log'],
                'propagate': True,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['console', 'mail_admins', 'request_log', 'log_warning'],
                'level': 'WARNING',
                'propagate': False,
            },
            
        }
    }

    logging.config.dictConfig(LOGGING)


class Development(Common):
    """
    The in-development settings and the default configuration.
    """
    DEBUG = True

    ALLOWED_HOSTS = []

    INTERNAL_IPS = [
        '127.0.0.1'
    ]

    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'debug_toolbar',
     ]

    MIDDLEWARE = Common.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    SESSION_COOKIE_SECURE = False

class Staging(Common):
    """
    The in-staging settings.
    """
    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(False)
    # SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    # SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    # SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    # SECURE_REDIRECT_EXEMPT = values.ListValue([])
    # SECURE_SSL_HOST = values.Value(None)
    # SECURE_SSL_REDIRECT = values.BooleanValue(False)
    # SECURE_PROXY_SSL_HEADER = values.TupleValue(
    #     ('HTTP_X_FORWARDED_PROTO', 'https')
    # )
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False
    ALLOWED_HOSTS = values.ListValue(
        ['*'])


class Production(Staging):
    """
    The in-production settings.
    """
    # Email
    EMAIL_HOST = values.Value(None)
    EMAIL_PORT = values.IntegerValue(456)
    EMAIL_HOST_USER = values.Value(None)
    EMAILEMAIL_USE_TLS = values.BooleanValue(True)
    EMAIL_USE_SSL = values.BooleanValue(False)
    SERVER_EMAIL = values.Value(None)
    CORS_REPLACE_HTTPS_REFERER      = False
    HOST_SCHEME                     = "http://"
    SECURE_PROXY_SSL_HEADER         = None
    SECURE_SSL_REDIRECT             = False
    SESSION_COOKIE_SECURE           = False
    CSRF_COOKIE_SECURE              = False
    SECURE_HSTS_SECONDS             = None
    SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
    SECURE_FRAME_DENY               = False
    # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
    

