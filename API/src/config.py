# /src/config.py

import os


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "azertdfgh"
    SQLALCHEMY_DATABASE_URI = "postgres://valibert:admin@127.0.0.1:5432/travelapidb"


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgres://valibert:admin@127.0.0.1:5432/travelapidb"
    JWT_SECRET_KEY = "azertdfgh"


class Testing(object):
    """
    Development environment configuration
    """
    TESTING = True
    JWT_SECRET_KEY = "azertdfgh!"
    SQLALCHEMY_DATABASE_URI = "postgres://valibert:admin@127.0.0.1:5432/travelapidb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': Development,
    'production': Production,
    'testing': Testing
}
