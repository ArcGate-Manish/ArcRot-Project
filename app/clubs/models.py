from sqlalchemy import text
from sqlalchemy.orm import lazyload
from datetime import datetime
from .. import db


class Club(db.Model):
    """This class represents clubs table in the database.
    This stores all the information related to the clubs."""

    __tablename__ = 'clubs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text, nullable=True)
    email_id = db.Column(db.String(255), nullable=False, unique=True)
    assistant_governor = db.Column(db.String(255), nullable=False)
    club_ids = db.Column(db.String(255), nullable=False)
    club_type = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False, unique=False)
    district_code = db.Column(db.Integer, nullable=False, unique=True)
    chartered = db.Column(db.Integer, nullable=False, unique=False)
    phone_no = db.Column(db.BigInteger, nullable=True)
    fax_no = db.Column(db.BigInteger, nullable=True)
    vendors = db.Column(db.String(255), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    rotary_langauge = db.Column(db.String(255), nullable=True)
    mailing_address = db.Column(db.String(255), nullable=True)
    is_active = db.Column(db.SmallInteger, default=1,
                          nullable=False, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now,
                           nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = db.Column(db.DateTime, default=datetime.now,  onupdate=datetime.now, nullable=False,
                           server_default=text('CURRENT_TIMESTAMP'))
    club_members = db.relationship(
        'ClubMembers', backref='Club', lazy='joined')

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
        return f"<Club {self.id}: {self.name}>"

    def getClubById(id):
        return Club.query.options(lazyload(Club.club_members)).filter_by(id=id).first()

    def getAllClub():
        return Club.query.options(lazyload(Club.club_members)).all()

    def getTotalClub():
        return len(Club.query.all())


class ClubMembers(db.Model):
    """This table represents the club_members table in the database.
    This stores the data of member associated with any club."""

    __tablename__ = 'club_members'

    id = db.Column(db.Integer, primary_key=True)
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'), nullable=False)
    club_member_id = db.Column(db.Integer, nullable=True, unique=True)
    member_first_name = db.Column(db.String(255), nullable=False)
    member_last_name = db.Column(db.String(255), nullable=True)
    member_from = db.Column(db.DateTime, default=datetime.now,
                            nullable=False, server_default=text('CURRENT_TIMESTAMP'), index=True)
    profile = db.Column(db.String(255), nullable=False)
    club_member_email = db.Column(db.String(255), nullable=False, unique=True)
    member_till = db.Column(db.DateTime, default=datetime.now, nullable=False,
                            server_default=text('CURRENT_TIMESTAMP'), onupdate=datetime.now)
    club_memb_is_active = db.Column(db.Boolean, default=0,
                                    nullable=False, index=True)
    profile_picture = db.Column(db.String(255), nullable=True)

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
        return f"<Club Id: {self.id}, Member Id: {self.club_member_id}>"

    def getTotalMember():
        return len(ClubMembers.query.all())
