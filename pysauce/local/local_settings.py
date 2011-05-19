import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROD = False
USE_SSL = False

LOCAL_PATH = os.path.dirname(os.path.abspath(__file__))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(LOCAL_PATH, 'dashboard_openstack'),
    },
}

CACHE_BACKEND = 'dummy://'

NOVA_DEFAULT_ENDPOINT = 'http://localhost:8773/services/Cloud'
NOVA_DEFAULT_REGION = 'nova'
NOVA_ACCESS_KEY = 'admin'
NOVA_SECRET_KEY = 'admin'
NOVA_ADMIN_USER = 'admin'
NOVA_PROJECT = 'admin'
