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
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", None),
        "HOST": "db_rblog",
        "PORT": "5432",
    }
}

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, "..", "rblog-media-files"))
