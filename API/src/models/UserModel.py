# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db

from .DreamModel import DreamModelSchema


class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    pseudo = db.Column(db.String(50), nullable=False)
    pass = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    dream = db.relationship('DreamModel', backref='users', lazy=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.pseudo = data.get('pseudo')
        self.password = self.__generate_hash(data.get('password'))
        self.mail = data.get('mail')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
        if key == 'password':  # add this new line
            self.password = self.__generate_hash(value)  # add this new line
        setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

    @staticmethod
    def get_user_by_email(value):
        return UserModel.query.filter_by(email=value).first()

    def __repr(self):
        return '<id {}>'.format(self.id)


class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    pseudo = fields.Str(required=True)
    password = fields.Str(required=True)
    mail = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    dream = fields.Nested(DreamSchema, many=True)
