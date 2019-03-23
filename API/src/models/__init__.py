from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.declarative import declarative_base

# initialise db
db = SQLAlchemy()
bcrypt = Bcrypt()


# creation de l'association
dream_cat = db.Table('dream_cat', 
                     db.Column('dream_id', db.Integer,
                               db.ForeignKey('dream.idDream')),
                     db.Column('cat_id', db.Integer,
                               db.ForeignKey('catdream.idCat'))
                     )

dream_cattransp = db.Table('dream_cattransp',
                           db.Column('dream_id', db.Integer,
                                     db.ForeignKey('dream.idDream')),
                           db.Column('cattransp_id', db.Integer,
                                     db.ForeignKey('cattransp.idCattransp'))
                           )

from .UserModel import UserModel, UserSchema
from .DreamModel import DreamModel, DreamSchema
