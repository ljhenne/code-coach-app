# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'service': '~/.pg_service.conf',
            'passfile': '~/.pgpass'
        }
    }
}
