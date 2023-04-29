import pytest

from app import create_app
from app.config import TestConfig
from app import db


@pytest.fixture
def app():
    app = create_app(TestConfig)
    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    client.environ_base['HTTP_X_API_KEY'] = TestConfig.SECRET_KEY
    return client


@pytest.fixture
def unsafe_client(app):
    return app.test_client()


@pytest.fixture
def db_session(app):
    with app.app_context():
        db.create_all()
        session = db.session
        yield session
        session.rollback()
        db.drop_all()
