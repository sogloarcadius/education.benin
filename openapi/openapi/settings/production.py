from openapi.settings.base import *
from corsheaders.defaults import default_headers

DEBUG = False

ALLOWED_HOSTS = ['.sogloarcadius.com',]

INSTALLED_APPS += ['corsheaders']

MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

CORS_ALLOW_HEADERS = default_headers + (
    'Cache-Control',
)

CORS_ORIGIN_ALLOW_ALL = True
