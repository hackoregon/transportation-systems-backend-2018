import pytest
import os
import transportation_systems_2018

@pytest.fixture(scope='session')
def django_db_setup():
    transportation_systems_2018.settings.DATABASES['default'] = {
        'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
        'CONN_MAX_AGE': 0,
        'OPTIONS': {
            'MAX_CONNS': 20
        }
    }
    transportation_systems_2018.settings.DATABASES['odot_crash_data'] = {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'OPTIONS': {
                'options': '-c search_path=django,odot_crash_data'
            },
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT')
    }
