from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()

DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DB_SECRET_KEY')

DEBUG = True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
