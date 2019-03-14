# src/models/DreamModel.py
from marshmallow import fields, Schema
import datetime
from . import db


class DreamModel(db.Model):
    """
    Dream Model
    """
    # table
    __tablename__ = "dream"

    idDream = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    adress = db.Column(db.String(255), nullable=False)
    note = db.Column(db.Text)
    travel = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.String(128))
    infoTransport = db.Column(db.Text)
    costTransport = db.Column(db.Float)
    accommodation = db.Column(db.Text)
    costAccommodation = db.Column(db.Float)
    whatTodo = db.Column(db.Text)
    whereToEat = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.img = data.get('img')
        self.country = data.get('country')
        self.adress = data.get('adress')
        self.note = data.get('note')
        self.travel = data.get('travel')
        self.date = data.get('date')
        self.infoTransport = data.get('infoTransport')
        self.costTransport = data.get('costTransport')
        self.accommodation = data.get('accommodation')
        self.costAccommodation = data.get('costAccommodation')
        self.whatTodo = data.get('whatTodo')
        self.whereToEat = data.get('whereToEat')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()
        self.owner_id = data.get('owner_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        de.session.commit()

    @staticmethod
    def get_all_dream():
        return DreamModel.query.all()

    @staticmethod
    def get_one_dream(id):
        return DreamModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class DreamSchema(Schema):
    """
        Dream Schema
    """
    idDream = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    img = fields.Str(required=True)
    country = fields.Str(required=True)
    adress = fields.Str(required=True)
    note = fields.Str()
    travel = fields.Boolean(required=True)
    date = fields.Str()
    infoTransport = fields.Str()
    costTransport = fields.Float()
    accommodation = fields.Str()
    costAccommodation = fields.Float()
    whatTodo = fields.Str()
    whereToEat = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    owner_id = fields.Int(required=True)
