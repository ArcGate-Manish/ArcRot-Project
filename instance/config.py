import os
from app import app

SECRET_KEY = 'thisissecretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# username = app.config['DATABASEUSERNAME']
# password = app.config['DATABASEPASSWORD']
host = app.config['DATABASEHOST']
SQLALCHEMY_DATABASE_URI = 'postgresql://bviwwdeagkitha:a7b649bd876f2112e748256b970c42bf182b4ce7e25aba0dce79d089d4cff005@ec2-54-87-249-251.compute-1.amazonaws.com:5432/d6ukapbi28kue9'

# SQLALCHEMY_DATABASE_URI = 'postgresql://stonex:ArcInd#123@localhost/rotary_udz'    
