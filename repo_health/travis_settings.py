from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'repo_health',
        'USER': 'root',
        'PASSWORD': '',
    }
}

# Settings for sqlite3 tests will use an in memory database and decrease test time.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'test',
#     }
# }
