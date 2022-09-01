import os
from app import app

SECRET_KEY = 'thisissecretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False
username = app.config['DATABASEUSERNAME']
password = app.config['DATABASEPASSWORD']
host = app.config['DATABASEHOST']
SQLALCHEMY_DATABASE_URI = 'postgresql://'+username+':'+password+'@localhost/rotary_udz'
    
    # 'connect_args': {
        # 'connect_timeout': 150
    # }
# }
