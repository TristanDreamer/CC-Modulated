from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

from. import events, routes

app.register_blueprint(events.bp)
app.register_blueprint(routes.bp)

@app.route("/test")
def test():
    from flask import render_template
    return render_template("root.html")
    return "<p1>Test</p1>"