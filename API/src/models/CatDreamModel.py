from marshmallow import fields, Schema
from . import db
from . import dream_cat


class CatDreamModel(db.Model):
    """
        Catégorie de rêve
    """

    # table name
    __tableaname__ = "catdream"

    idCat = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    fk_dream = db.relationship(
        'DreamModel', secondary=dream_cat, back_populates='catdream')

    def __init__(self, data):
        """
         Class constructor
        """
        self.name = data.get("name")
        self.fk_dream = data.get('fk_dream')

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


class CatDreamSchema(Schema):
    """
    CatDream schema
    """
    idCat = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    fk_dream = fields.Nested("DreamSchema", many=True, exclude=('fk_catdream',))
