from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "blog",
#         "USER": "blog",
#         "PASSWORD": "blog",
#         "HOST": "127.0.0.1",
#         "PORT": "5432",
#     },
# }

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
