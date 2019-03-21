from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialise db
db = SQLAlchemy()
bcrypt = Bcrypt()

# creation de l'association
dream_cat = db.Table('dream_cat', Base.metadata,
                     db.Column('dream_id', Integer,
                               ForeignKey('dream.idDream')),
                     db.Column('cat_id', Integer,
                               ForeignKey('catdream.idCat'))
                     )
dream_cattransp = db.Table('dream_cattransp', Base.metadata,
                           db.Column('dream_id', Integer,
                                     ForeignKey('dream.idDream')),
                           db.Column('cattransp_id', Integer,
                                     ForeignKey('cattransp.idCattransp'))
                           )
