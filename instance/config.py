import os
from app import app

SECRET_KEY = 'thisissecretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False
username = app.config['DATABASEUSERNAME']
password = app.config['DATABASEPASSWORD']
host = app.config['DATABASEHOST']
SQLALCHEMY_DATABASE_URI = 'mysql://' + username + ':' + password + '@' + host + '/rotary_udz'
SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'connect_timeout': 150
    }
}