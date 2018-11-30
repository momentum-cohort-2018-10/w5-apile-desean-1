from apile.settings import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

import django_heroku
django_heroku.settings(locals())
