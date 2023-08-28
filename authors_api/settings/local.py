from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
# generate secret key using command: python -c "import secrets; print(secrets.token_urlsafe(38))"
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="dfiWBAxU5kUOdoXKqUHpvw9sazOnKLsU23pme6yX1N6mP_j5AvQ0",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
