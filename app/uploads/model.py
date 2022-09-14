from datetime import datetime
from sqlalchemy import text
from .. import db
from sqlalchemy.orm import relationship



# class Uploads (db.Model, Image):
#     """This class represents uploads table in the database.
#    This stores all the information related to the file name, 
#    file path and profile id of club members."""

#     __tablename__ = 'uploads'
#     id = db.Column(db.Integer, primary_key=True)
#     profile_id = db.Column(db.Integer, db.ForeignKey(
#         'club_members.id'), nullable=False, index=False)
#     file_name = db.Column(db.String(255), nullable=False)
#     path = db.Column(db.Text(), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.now,
#                            nullable=True, index=True,
#                            server_default=text('CURRENT_TIMESTAMP'))
#     updated_at = db.Column(db.DateTime, default=datetime.now,
#                            onupdate=datetime.now, nullable=False,
#                            server_default=text('CURRENT_TIMESTAMP'))

#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#         return self

#     def update(self):
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def __repr__(self):
#         return f"<Event: {self.id}>"
