# coding: utf-8
__author__ = 'Paul Cunningham'
__copyright__ = 'Copyright 2018, Paul Cunningham'

import email
from flask import current_app
from flask.cli import click, with_appcontext
from flask_security.utils import hash_password
from . import db
from .. import Role, User

@click.command(name='create_database')
@with_appcontext
def create_database():
    security = current_app.extensions.get('security')

    # db.drop_all()
    db.create_all()

    user_role = Role(name='user')
    super_user_role = Role(name='superuser')
    db.session.add(user_role)
    db.session.add(super_user_role)
    db.session.commit()

    test_user = security.datastore.create_user(
        first_name='Admin',
        email = 'admin',
        password=hash_password('admin'),
        roles=[user_role, super_user_role]
    )
    db.session.commit()
