from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True

DATABASES = {
    # 'users': {
    #     'ENGINE': 'django.db.backends.mysql',  # django.db.backends.sqlite3
    #     'NAME': 'fangxiongreal', #  os.path.join(BASE_DIR, 'db.sqlite3')
    #     'USER': 'root',  # fangxiongreal
    #     'PASSWORD': 'a',  # 0000
    #     'HOST': '127.0.0.1',  #
    #     'PORT':'3306',
    # },
    # The following users database is not being employed
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #    },
        
        
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fangxiongreal',
        'USER': 'root',
        'PASSWORD': 'a',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True, },
    }
}


