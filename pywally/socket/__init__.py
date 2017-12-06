from flask_socketio import SocketIO

from .handlers import init_handlers

def init_socket(app):
    socketio = SocketIO(app, debug=True)
    init_handlers(socketio)
    socketio.run(app)
    return socketio
