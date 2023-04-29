from app.database import db

from .user import User

models = {
    'User': User,
}


def init_db(app):
    with app.app_context():
        db.create_all()
