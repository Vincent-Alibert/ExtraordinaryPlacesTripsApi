from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.declarative import declarative_base

# initialise db
db = SQLAlchemy()
bcrypt = Bcrypt()

from .UserModel import UserModel, UserSchema
from .DreamModel import DreamModel, DreamSchema
