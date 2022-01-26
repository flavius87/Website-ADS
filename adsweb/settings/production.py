from .base import*

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['adsweb.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5esspj9bgjc2o',
        'USER': 'gyhfitolypdaky',
        'PASSWORD': 'd127d6a8a2fe0696a45cc7a357dfa994f96cc03e559f8092e052f1e10f93af28',
        'HOST': 'ec2-52-45-83-163.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

