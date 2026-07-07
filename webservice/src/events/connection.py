from ..main import sock

@sock.route("/connected")
def connection(ws):
    ws.send("Connected!")
   
    while ws.connected:
        data = input("Server > ")
        print(ws.connected)
        ws.send(data)
        if data == "end":
            break