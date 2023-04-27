import os

from dotenv import load_dotenv


load_dotenv()


def database_url() -> str:
    host = os.environ.get("DB_HOST", "127.0.0.1")
    port = os.environ.get("DB_PORT", 3306)
    database = os.environ.get("DB_DATABASE", "todos")
    user = os.environ.get("DB_USER", "root")
    password = os.environ.get("DB_PASSWORD", "root")

    return f"mysql://{user}:{password}@{host}:{port}/{database}"


def redis_url() -> str:
    host = os.environ.get("REDIS_HOST", "127.0.0.1")
    port = os.environ.get("REDIS_PORT", 6379)

    return f"redis://{host}:{port}"


class Config(object):
    SQLALCHEMY_DATABASE_URI = database_url()
    CACHE_TYPE = os.environ.get("CACHE_TYPE", "FileSystemCache")
    CACHE_REDIS_URL = redis_url()
    CACHE_DIR = os.environ.get("CACHE_DIR", "cache")
