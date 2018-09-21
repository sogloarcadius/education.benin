from openapi.settings.base import *
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = default_headers + (
    'Cache-Control',
)

CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True
ALLOWED_HOSTS = ["*"]
