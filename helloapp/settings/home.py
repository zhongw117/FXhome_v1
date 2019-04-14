from .base import *

DEBUG = True


DATABASES = {

    # The following users database is not being employed
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     },

     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fangxiongreal',
        'USER': 'root',
        'PASSWORD': 'abcd@0123',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'use_unicode': True, },
    }
}
