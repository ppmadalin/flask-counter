import os

SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_NAME = os.environ['DATABASE_NAME']
DB_URI = 'sqlite:///instances/counter.db'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
