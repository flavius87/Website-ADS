from .base import*
from decouple import config

DEBUG = config('DEBUG')
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=config('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD') 
EMAIL_PORT=587