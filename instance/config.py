import os
from app import app

SECRET_KEY = 'thisissecretkey'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# username = app.config['DATABASEUSERNAME']
# password = app.config['DATABASEPASSWORD']
host = app.config['DATABASEHOST']
# SQLALCHEMY_DATABASE_URI = 'postgresql://qegfnzlagugend:c7909bb6b024745da4c0809a3484f7152c154d78d55ba52dd026d200bad5f6ac@ec2-44-205-64-253.compute-1.amazonaws.com:5432/dcle927379napd'

SQLALCHEMY_DATABASE_URI = 'postgresql://stonex:ArcInd#123@localhost/rotary_udz'    
