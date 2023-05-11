import os


def database_url() -> str:
    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", 3306)
    database = os.getenv("DB_DATABASE", "todos")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "root")

    return f"mysql://{user}:{password}@{host}:{port}/{database}"
