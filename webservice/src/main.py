from app import create_app, socketio

app = create_app()

@app.route("/")
def landing():
    return '<h1>This is the landing page</h1>'

if __name__ == '__main__':
    socketio.run(app)