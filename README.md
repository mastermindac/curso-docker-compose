# Development Setup

## Backend

Install all the requirements:
- [Python](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [MySQL](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)
- [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

Copy `.env` file and change the values if needed:
```bash
cd backend
cp .env.example .env
```

Install dependencies:
```bash
export PIPENV_VENV_IN_PROJECT=1
pipenv install 
```

Run migrations:
```bash
export FLASK_APP=flasktodos/app.py
pipenv run flask db upgrade
```
Start the server:

```bash
pipenv run flask --debug run
```

Flask API will be running on [`http://127.0.0.1:5000`](http://127.0.0.1:5000).

## Frontend

Install all the requirements:

- [Node.js](https://nodejs.org/en/download/package-manager)

Copy `.env` file and change the values if needed:
```bash
cd frontend
cp .env.example .env
```

Install dependencies:
```bash
npm install
```

Start the server:

```bash
npm run dev
```

Vite server will be running on [`http://127.0.0.1:5173`](http://127.0.0.1:5173).
