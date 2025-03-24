from config.django.base import *
from config.env import env

DEBUG = env.bool("DJANGO_DEBUG", default=False)

SECRET_KEY = env.str("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])

CACHES = {"default": env.cache("REDIS_CACHE_URL", default="redis://localhost:6379")}
