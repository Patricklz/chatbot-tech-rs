from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO


db = SQLAlchemy()
socketio = SocketIO(cors_allowed_origins="*", async_mode='eventlet')


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    socketio.init_app(app) 

    from src.controllers.chatbot_controller import chatbot_bp
    app.register_blueprint(chatbot_bp)

    import src.websocket.chatbot_socket

    return app