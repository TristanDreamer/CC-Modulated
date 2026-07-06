from flask_socketio import emit
from .. import socketio

@socketio.on('connect')
def test_connect(auth):
    print("Connection!")
    emit('my response', {'data': 'Connected'})
    
@socketio.on('disconnect')
def test_disconnect(reason):
    print('Client disconnected, reason:', reason)