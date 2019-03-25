from marshmallow import fields, Schema
import datetime
from . import db
from .CatDreamModel import CatDreamModel 
from .CatTransportModel import CatTransportModel 

dream_cat = db.Table('dreamcat',
                     db.Column('dream_id', db.Integer, db.ForeignKey('dream.idDream'), primary_key=True),
                     db.Column('cat_id', db.Integer, db.ForeignKey('catdream.idCat'), primary_key=True)
                     )


dream_cattransp = db.Table('dreamcattransp', 
                           db.Column('dream_id', db.Integer,
                                     db.ForeignKey('dream.idDream'), primary_key=True),
                           db.Column('cattransp_id', db.Integer,
                                     db.ForeignKey('cattransp.idCatTransp'), primary_key=True)
                           )

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
    createdAt = db.Column(db.DateTime)
    modifiedAt = db.Column(db.DateTime)
    # définition des relations
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    catOfDream = db.relationship(
        'CatDreamModel', secondary=dream_cat, backref=db.backref('dreams', lazy='dynamic'))
    catOfTransport = db.relationship(
        'CatTransportModel', secondary=dream_cattransp, backref=db.backref('dreams', lazy='dynamic'))

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
        self.createdAt = datetime.datetime.utcnow()
        self.modifiedAt = datetime.datetime.utcnow()
        self.user = data.get('user')
        self.catOfDream = data.get('catOfDream')
        self.catOfTransport = data.get('catOfTransport')

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

    def __repr__(self):
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
    fk_user = fields.Int(required=True)

    fk_catdream = fields.Nested('CatDreamSchema', many=True)
    fk_cattransport = fields.Nested('CatTransportSchema', many=True)
