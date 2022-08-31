import os
from app import app

SECRET_KEY = 'thisissecretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False
username = app.config['DATABASEUSERNAME']
password = app.config['DATABASEPASSWORD']
host = app.config['DATABASEHOST']
SQLALCHEMY_DATABASE_URI = 'postgres://ahaanyvcethfxn:8c9b497700d1e5dbcb5f22e78905d1fd6d78c21e834cf434c28db5409f4877bf@ec2-44-205-112-253.compute-1.amazonaws.com:5432/ddrlufbkeg6qs8'
SQLALCHEMY_ENGINE_OPTIONS = {
    'connect_args': {
        'connect_timeout': 150
    }
}