from apile.settings import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'https://serene-river-53724.herokuapp.com/', 'https://arcane-mesa-74274.herokuapp.com/']

import django_heroku
django_heroku.settings(locals())
