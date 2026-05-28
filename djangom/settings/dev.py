from .common import *
from dotenv import load_dotenv
import os
import pymysql

pymysql.install_as_MySQLdb()

load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG")
PRODUCTION = os.environ.get('PRODUCTION')
DB_HOST = os.environ.get('DB_HOST')

if DB_HOST: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': DB_HOST,
            'PORT': os.environ.get('DB_PORT', '3306'),
            "OPTIONS": {
                "init_command": "SET default_storage_engine=INNODB",
            }
        }
    }
else:
        DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            "OPTIONS": {
                "init_command": "SET default_storage_engine=INNODB",
            }
        }
    }

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media')
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
