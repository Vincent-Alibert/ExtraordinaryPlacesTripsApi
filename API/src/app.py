from flask import Flask
from .config import app_config
from .models import db, bcrypt


def create_app(env_name):
    """
    Creation de l'application
    """
    # app initialisation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    bcrypt.init_app(app)
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def index():
        """
            test app
        """
        return 'app working'

    return app
