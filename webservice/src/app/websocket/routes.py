from . import bp

@bp.route("/listen")
def listen():
    return {"message":"Connection Success"}

@bp.route("/")
def root():
    return "<p>Welcome to the websocket!</p1>"