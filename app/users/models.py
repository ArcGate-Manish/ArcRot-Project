from datetime import datetime
from sqlalchemy import text
from sqlalchemy.orm import lazyload
from flask_security import UserMixin, RoleMixin
from .. import db


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer,
                                 db.ForeignKey('users.id'), primary_key=True),
                       db.Column('role_id', db.Integer, db.ForeignKey('roles.id'), primary_key=True))


class Role(db.Model, RoleMixin):
    """This class represents roles table in database.
    It stores all the roles of users."""

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    role_created_at = db.Column(db.DateTime, default=datetime.now, index=True,
                           server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, default=datetime.now,
                           onupdate=datetime.now,
                           server_default=text('CURRENT_TIMESTAMP'))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<Role {self.id}: {self.name}>'


class User(db.Model, UserMixin):
    """This class represents users table in database.
    It stores all the details of users."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=True)
    image_name = db.Column(db.String(255), nullable=True, unique=True)
    city = db.Column(db.String(255), nullable=True)
    contact_number = db.Column(db.BigInteger, nullable=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.SmallInteger, default=1,
                          nullable=False, index=True)
    active= db.Column(db.Boolean,nullable = False, default = True)
    user_created_at = db.Column(db.DateTime, default=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.now)
    author = db.relationship('Author', backref='users', lazy='joined')
    roles = db.relationship('Role', secondary=roles_users,
                           backref='users', lazy='joined')

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id}: {self.first_name} {self.last_name}>"

    def getUserById(id):
        return User.query.options(lazyload(User.author)).options(lazyload(User.roles)).filter_by(id = id).first()


    def getAllUser():
        return User.query.options(lazyload(User.author)).options(lazyload(User.roles)).all()
