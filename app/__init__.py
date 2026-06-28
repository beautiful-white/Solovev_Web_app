from flask import Flask
from .database import init_db


def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "super_secret_key_123"

    with app.app_context():
        init_db()

    from .routes import bp
    app.register_blueprint(bp)

    return app
