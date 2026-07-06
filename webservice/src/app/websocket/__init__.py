import flask

bp = flask.Blueprint("websocket", __name__, url_prefix="/websocket")

from . import events, routes