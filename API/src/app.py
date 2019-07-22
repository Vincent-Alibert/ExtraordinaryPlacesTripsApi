# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS, cross_origin
from .config import app_config
from .models import db, bcrypt
from .controler.UserView import user_api as user_blueprint
from .controler.DreamView import dream_api as dream_blueprint
from .controler.CatDreamView import catdream_api as catdream_blueprint
from .controler.CatTransportView import cattransp_api as cattransp_blueprint


def create_app(env_name):
    """
    Creation de l'application
    """
    # app initialisation
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(app_config[env_name])
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
    app.register_blueprint(dream_blueprint, url_prefix='/api/v1/dreams')
    app.register_blueprint(catdream_blueprint, url_prefix='/api/v1/catdream')
    app.register_blueprint(cattransp_blueprint, url_prefix='/api/v1/cattransp')

    @app.route('/', methods=['GET'])
    def index():
        """
            test app
        """
        return 'app working'

    return app
