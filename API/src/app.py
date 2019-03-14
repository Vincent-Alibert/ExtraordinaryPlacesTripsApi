from flask import Flask
from .config import app_config


def create_app(env_name):
    """
    Creation de l'application
    """
    # app initialisation
    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    @app.route('/', methods=['GET'])
    def index():
        """
            test app
        """
        return 'app working'

    return app
