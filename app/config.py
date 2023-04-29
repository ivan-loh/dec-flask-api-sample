import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mssql+pymssql://sa:devDBpassword!%40#$@localhost:1433/devdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
