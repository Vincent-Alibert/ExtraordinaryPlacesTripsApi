# -*- coding: utf-8 -*-
from marshmallow import fields, Schema
from . import db
import datetime

class CatTransportModel(db.Model):
    """
        Catégorie de transport
    """

    # table name
    __tablename__ = "cattransp"

    idCatTransp = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    

    def __init__(self, data):
        """
         Class constructor
        """
        self.name = data.get("name")
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

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
    def get_one_cat(name):
        """
        Get one catégorie by name
        """
        return CatTransportModel.query.filter_by(name=name).first()


class CatTransportSchema(Schema):
    """
    CatTransport Schema
    """
    idCatTransp = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    #dreams = fields.Nested("DreamSchema", only=["name"], many=True)
    