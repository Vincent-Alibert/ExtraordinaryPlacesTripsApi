from marshmallow import fields, Schema
from . import db


class CatTransportModel(db.Model):
    """
        Catégorie de transport
    """

    # table name
    __tablename__ = "cattransp"

    idCatTransp = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    

    def __init__(self, data):
        """
         Class constructor
        """
        self.name = data.get("name")

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
    def get_one_cat(idCat):
        return CatDream.query.get(idCat)


class CatTransportSchema(Schema):
    """
    CatTransport Schema
    """
    idCat = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    dreams = fields.Nested("DreamSchema", many=True, exclude=('catOfTransport',))
