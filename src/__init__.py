from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from src.controllers.chatbot_controller import chatbot_bp
    app.register_blueprint(chatbot_bp)

    return app