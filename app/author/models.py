from datetime import datetime
from sqlalchemy import text
from sqlalchemy.orm import lazyload
from .. import db


class Author(db.Model):
    """This class represents author's table in database.
    It stores all the details of authors."""
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False, unique=True, index=True)
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now,
                           nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.now)
    posts = db.relationship('Post', backref='author', lazy='joined')

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
        return f"<Author: {self.id}, User id: {self.user_id}>"

    def getAuthorById(id):
        return Author.query.options(lazyload(Author.posts)).filter_by(id = id).first()


    def getAllAuthor():
        return Author.query.options(lazyload(Author.posts)).all()
