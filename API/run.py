import os

from src.app import create_app

if __name__ == '__main__':
    env_name = "development"
    app = create_app(env_name)
    app.run(host="192.168.43.171", port=5000)


