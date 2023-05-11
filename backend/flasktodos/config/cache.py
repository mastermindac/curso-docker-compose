import os


def redis_url() -> str:
    host = os.getenv("REDIS_HOST", "127.0.0.1")
    port = os.getenv("REDIS_PORT", 6379)

    return f"redis://{host}:{port}"
