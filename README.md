# Development Setup

## Backend

Requirements:
- [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [MySQL](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)
- [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

Dependencies:
```bash
cd backend
export PIPENV_VENV_IN_PROJECT=1
pipenv install 
```

Migrations:
```bash
export FLASK_APP=todos/app.py
pipenv run flask db upgrade
```
Server:

```bash
pipenv run flask --debug run
```

Flask API will be running on `127.0.0.1:5000`.

## Frontend

Requirements:

- [Node.js](https://nodejs.org/en/download/package-manager)

Dependencies:

```bash
cd frontend
npm install
```

Server:

```bash
npm run dev
```

Vite server will be running on `127.0.0.1:5173`.
