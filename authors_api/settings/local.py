from .base import *  # noqa
from .base import env


# generate secret key using command: python -c "import secrets; print(secrets.token_urlsafe(38))"
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="dfiWBAxU5kUOdoXKqUHpvw9sazOnKLsU23pme6yX1N6mP_j5AvQ0",
)

ALLOWED_HOSTS = ["*"]

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@apiimperfect.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
