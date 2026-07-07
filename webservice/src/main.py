from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

from. import events, routes

app.register_blueprint(events.bp)
app.register_blueprint(routes.bp)

print(app.root_path)
print(app.static_folder)
print(app.template_folder)