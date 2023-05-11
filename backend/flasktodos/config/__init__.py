import os

from .cache import redis_url
from .database import database_url


class Config(object):
    SQLALCHEMY_DATABASE_URI = database_url()

    CACHE_TYPE = os.getenv("CACHE_TYPE", "FileSystemCache")
    CACHE_DIR = os.getenv("CACHE_DIR", "cache")
    CACHE_REDIS_URL = redis_url()

    JWT_ACCESS_SECRET = os.getenv("JWT_ACCESS_SECRET", "dev_access_secret")
    JWT_REFRESH_SECRET = os.getenv("JWT_REFRESH_SECRET", "dev_refresh_secret")
    CORS_ALLOW_ORIGIN = os.getenv("CORS_ALLOW_ORIGIN", None)
