"""
Django settings for runna project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
from datetime import timedelta

RESEND_API_KEY = config("RESEND_API_KEY")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y=k)d^2rlms)+dg!5a3aiygxsorf##qk6=p0&%d33$$2@(2!0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

    # unfold dependencies
    "unfold",  # before django.contrib.admin
    "unfold.contrib.filters",  # optional, if special filters are needed
    "unfold.contrib.forms",  # optional, if special form elements are needed
    "unfold.contrib.inlines",  # optional, if special inlines are needed
    "unfold.contrib.import_export",  # optional, if django-import-export package is used
    "unfold.contrib.guardian",  # optional, if django-guardian package is used
    "unfold.contrib.simple_history",  # optional, if django-simple-history package is used

    # built-in django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # custom apps
    'services',
    'customAuth',
    'infrastructure',
    'api',
    'admin_custom',
    
    # restframework dependencies
    'rest_framework',
 
    # third-party dependencies
    'corsheaders',  # to enable CORS
    
    # track model changes
    'simple_history',

    'drf_spectacular',
    'drf_spectacular_sidecar',  # For Swagger UI assets
    
    'admin_reorder',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # corsheaders middleware    
    "corsheaders.middleware.CorsMiddleware",

    'runna.middleware.ThreadLocalMiddleware',

    'admin_reorder.middleware.ModelAdminReorder',
]

ADMIN_REORDER = [
    {
        'app': 'customAuth',
        'models': [
            "customAuth.TZona",
            "customAuth.CustomUser",
            "customAuth.TCustomUserZona",
        ]
    },
    {
        'app': 'infrastructure',
        'models': [
            "infrastructure.TLocalidad",
            "infrastructure.TBarrio",
            "infrastructure.TCPC",
            "infrastructure.TLocalizacion",

            "infrastructure.TBloqueDatosRemitente",
            "infrastructure.TTipoInstitucionDemanda",
            "infrastructure.TAmbitoVulneracion",
            "infrastructure.TTipoPresuntoDelito",
            "infrastructure.TInstitucionDemanda",
            "infrastructure.TDemanda",
            "infrastructure.TDemandaHistory",
            "infrastructure.TTipoCodigoDemanda",
            "infrastructure.TCodigoDemanda",
            "infrastructure.TCalificacionDemanda",
            "infrastructure.TCalificacionDemandaHistory",
            "infrastructure.TDemandaScore",
            "infrastructure.TDemandaScoreHistory",

            "infrastructure.TVinculoDePersonas",
            "infrastructure.TPersona",
            "infrastructure.TPersonaHistory",
            "infrastructure.TInstitucionEducativa",
            "infrastructure.TEducacion",
            "infrastructure.TEducacionHistory",
            "infrastructure.TInstitucionSanitaria",
            "infrastructure.TSituacionSalud",
            "infrastructure.TEnfermedad",
            "infrastructure.TMedico",
            "infrastructure.TCoberturaMedica",
            "infrastructure.TCoberturaMedicaHistory",
            "infrastructure.TPersonaEnfermedades",
            "infrastructure.TPersonaEnfermedadesHistory",
            "infrastructure.TNNyAScore",
            "infrastructure.TNNyAScoreHistory",
            "infrastructure.TLegajo",
            "infrastructure.TLegajoHistory",

            "infrastructure.TCategoriaMotivo",
            "infrastructure.TCategoriaSubmotivo",
            "infrastructure.TGravedadVulneracion",
            "infrastructure.TUrgenciaVulneracion",
            "infrastructure.TCondicionesVulnerabilidad",
            "infrastructure.TVulneracion",
            "infrastructure.TVulneracionHistory",

            "infrastructure.TLocalizacionPersona",
            "infrastructure.TLocalizacionPersonaHistory",
            "infrastructure.TDemandaPersona",
            "infrastructure.TDemandaPersonaHistory",
            "infrastructure.TDemandaZona",
            "infrastructure.TDemandaZonaHistory",
            "infrastructure.TDemandaVinculada",
            "infrastructure.TDemandaVinculadaHistory",
            "infrastructure.TPersonaCondicionesVulnerabilidad",
            "infrastructure.TPersonaCondicionesVulnerabilidadHistory",

            "infrastructure.TActividadTipo",
            "infrastructure.TInstitucionActividad",
            "infrastructure.TActividad",
            "infrastructure.TRespuesta",
            "infrastructure.TIndicadoresValoracion",
            "infrastructure.TEvaluaciones",
            "infrastructure.TDecision",
            "infrastructure.TActividadHistory",
            "infrastructure.TEvaluacionesHistory",
        ]
    },
]

ROOT_URLCONF = 'runna.urls'

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

WSGI_APPLICATION = 'runna.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS =  [
    "https://web-production-c6370.up.railway.app",
    "http://127.0.0.1:3000",  # Your Next.js frontend
    "http://localhost:3000",  # Your Next.js frontend
    "https://senaf-runna-nextjs-frontend-130125.vercel.app",
    "https://senaf-runna-nextjs-frontend-130125-29912tyxv-fo-sc.vercel.app",
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",  # Your Next.js frontend
    "http://localhost:3000",  # Your Next.js frontend
    "https://senaf-runna-nextjs-frontend-130125.vercel.app",
    "https://senaf-runna-nextjs-frontend-130125-29912tyxv-fo-sc.vercel.app",
]

CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://senaf-runna-nextjs-frontend-130125.vercel.app",
    "https://senaf-runna-nextjs-frontend-130125-29912tyxv-fo-sc.vercel.app",
]

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=600),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "TOKEN_OBTAIN_SERIALIZER": "customAuth.serializers.MyTokenObtainPairSerializer",
}

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True

# settings.py
AUTH_USER_MODEL = 'customAuth.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # Use drf-spectacular schema
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 5,  # Adjust as needed
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'


SPECTACULAR_SETTINGS = {
    'TITLE': 'RUNNA API',
    'DESCRIPTION': 'API documentation for the RUNNA re-Engineering project.',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': r'/api',  # Adjust based on your endpoint structure
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',  # or 'ERROR' for only errors
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/django.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['file', 'console'],  # Logs to both console and file
        'level': 'INFO',
    },
}



