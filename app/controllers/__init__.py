from .user import user_bp
from .system import system_bp


def register_blueprints(app):
    app.register_blueprint(user_bp, url_prefix='/api/v1')
    app.register_blueprint(system_bp, url_prefix='/api/v1')
