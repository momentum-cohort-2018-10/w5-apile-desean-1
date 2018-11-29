from apile.settings import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

import django_heroku
django_heroku.settings(locals())
