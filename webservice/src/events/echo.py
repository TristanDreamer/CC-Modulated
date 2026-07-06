from ..main import sock

@sock.route('/echo')
def echo(ws):
    """Returns whatever is sent through the websocket."""
    while ws.connected:
        data = ws.receive()
        ws.send(data)