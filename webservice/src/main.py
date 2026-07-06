from flask import Flask
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route("/")
def root():
    return "<p>Hello Mum!</p>"

@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)

@sock.route("/connected")
def connected(ws):
    ws.send("Connected!")
   
    while ws.connected:
        data = input("Server > ")
        print(ws.connected)
        ws.send(data)