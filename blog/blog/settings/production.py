from .base import *

DEBUG = False

ADMINS = [
    ("Yasin A", "yasin@test.com"),
]

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blog",
        "USER": "blog",
        "PASSWORD": "blog",
    },
}
