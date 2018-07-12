import os
from .dev import *

SECRET_KEY = os.environ.get("RBLOG_SECRET_KEY", None)
DEBUG = False
ALLOWED_HOSTS = [".raesener.de", ".räsener.de"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "rblog",
        "USER": "postgres",
        "PASSWORD": os.environ.get("RBLOG_POSTGRES_PASSWORD", None),
        "HOST": "db_rblog",
        "PORT": "5432",
    }
}
