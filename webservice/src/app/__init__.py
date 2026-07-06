from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug

    from .websocket import bp as websocket
    app.register_blueprint(websocket)

    socketio.init_app(app)
    return app
