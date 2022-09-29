from .. import db
from datetime import datetime
from sqlalchemy import text


class Event(db.Model):
    """This class represents event table in the database.
    This stores all the information related to the events."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=False)
    time = db.Column(db.DateTime, nullable=False, unique=False)
    address = db.Column(db.String(255), nullable=False, unique=False)
    event_created_at = db.Column(db.DateTime, default=datetime.now, index=True,
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
        return f"<Event: {self.id}>"

    def getEventById(id):
        return Event.query.filter_by(id=id).first()

    def getAllEvent():
        return Event.query.all()
