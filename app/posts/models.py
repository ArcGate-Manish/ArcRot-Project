from operator import ipow
from sqlalchemy import text
from datetime import datetime
from sqlalchemy.orm import lazyload
from .. import db


post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer,
                              db.ForeignKey('posts.id'), primary_key=True),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True))


class Tag(db.Model):
    """This class represents tags table in database.
    This stores all the tags/categories of the posts."""
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    tag_created_at = db.Column(db.DateTime, default=datetime.now,
                           nullable=False, server_default=text('CURRENT_TIMESTAMP'), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.now)

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
        return f"<Tag {self.name}>"


class Post(db.Model):
    """This class represents posts table in the database.
    It stores all the Post details."""

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'author.id'), nullable=False, index=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    cover_image_name = db.Column(db.String(255), nullable=False)
    post_created_at = db.Column(db.DateTime, default=datetime.now,
                           nullable=False, server_default=text('CURRENT_TIMESTAMP'), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.now)
    post_images = db.relationship('PostImages', backref='posts', lazy='joined')
    post_tags = db.relationship('Tag', secondary=post_tag, backref='posts',lazy ='joined')

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
        return f"<Post {self.id}>"

    
    def getPostById(id):
        return Post.query.options(lazyload(Post.post_tags)).options(lazyload(Post.post_images)).filter_by(id=id).first()

    def getAllPost():
        return Post.query.options(lazyload(Post.post_tags)).all()
    

class PostImages(db.Model):
    """This class represents post_images table in the database.
    It stores all the images of the Post except cover_image of the post."""

    __tablename__ = 'post_images'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.id'), nullable=False, index=True)
    image_name = db.Column(db.String(255), nullable=False)
    postimg_created_at = db.Column(db.DateTime, default=datetime.now,
                           nullable=False, server_default=text('CURRENT_TIMESTAMP'), index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.now)

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
        return f"<PostImages {self.id}>"
