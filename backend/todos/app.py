from flask import Flask
from flask_caching import Cache
from flask_cors import CORS

from .cache import cache
from .config import Config
from .database import db, migrate


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
migrate.init_app(app, db)

cache.init_app(app)

# Simple Package Structure
# https://flask.palletsprojects.com/en/2.3.x/patterns/packages/
import todos.handlers
import todos.views
