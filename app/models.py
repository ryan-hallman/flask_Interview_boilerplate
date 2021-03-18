from datetime import datetime

import names
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime

from app import db, bcrypt


class User(db.Model, UserMixin):

    """ A user who has an account on the website. """

    __tablename__ = 'users'

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String, primary_key=True)
    confirmation = db.Column(db.Boolean)
    _password = db.Column(db.String)
    create_date = db.Column(DateTime(timezone=True), server_default=func.now())

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def check_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.email


class Widgets(db.Model):

    """ Widgets table """

    __tablename__ = 'widgets'

    id = db.Column(db.Integer, primary_key=True)
    widget_name = db.Column(db.String)
    widget_value = db.Column(db.String)
    create_date = db.Column(DateTime(timezone=True), server_default=func.now())
    widget_updated_by = db.Column(db.String)

    @staticmethod
    def make_widgets(count):
        for i in range(count):
            new_widget = Widgets(
                widget_name=names.get_first_name(),
                create_date=datetime.now()
            )
            db.session.add(new_widget)
        db.session.commit()

    @classmethod
    def get_all_widgets(cls):
        return db.session.query(
            cls
        ).all()

