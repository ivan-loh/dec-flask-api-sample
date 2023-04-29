from flask import Flask, request
from app.controllers import register_blueprints
from app.models import init_db
from app.database import db
from app.config import Config

unsafe_routes = [
    '/api/v1/system/time'
]


def create_app(config_class=Config):
    # Create app
    app = Flask(__name__, static_url_path=None)
    app.config.from_object(config_class)

    # Authentication
    @app.before_request
    def route_check():
        print(request.path)
        if request.path not in unsafe_routes:
            return auth_check()

    def auth_check():
        secret_key = app.config.get("SECRET_KEY")
        if not secret_key:
            return

        api_key = request.headers.get('x-api-key')
        if not api_key or api_key != secret_key:
            return {'message': 'Unauthorized'}, 401

    # Setup
    db.init_app(app)
    init_db(app)
    register_blueprints(app)

    return app
