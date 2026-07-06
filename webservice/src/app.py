import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route("/")
def heartboat():
    return "<h1>Hello, I am alive!</h1>"

if __name__ == "__main__":
    socketio.run(app)