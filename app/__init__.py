from flask import Flask
from app.controllers import register_blueprints
from app.models import init_db
from app.database import db
from app.config import Config


def create_app(config_class=Config):

    app = Flask(__name__, static_url_path=None)
    app.config.from_object(config_class)
    db.init_app(app)

    init_db(app)
    register_blueprints(app)

    return app
