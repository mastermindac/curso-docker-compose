from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from flasktodos.cache import cache
from flasktodos.config import Config
from flasktodos.database import db, migrate
from flasktodos.errors import handlers
from flasktodos.views import auth, todos

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, origins=Config.CORS_ALLOW_ORIGIN, supports_credentials=True)

db.init_app(app)
migrate.init_app(app, db)

cache.init_app(app)

app.register_blueprint(handlers.blueprint)
app.register_blueprint(todos.blueprint, url_prefix="/todos")
app.register_blueprint(auth.blueprint, url_prefix="/auth")

@app.get("/")
def index():
    return {"message": "Flask Todos API"}
