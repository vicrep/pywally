from flask import request
from flask_socketio import join_room, leave_room, send, emit


def init_handlers(socket):
    @socket.on('join')
    def on_join_room(data):
        sid = data['session_id']
        cid = data['client_id']
        join_room(sid)
        emit("Client {} joined session {}".format(cid, sid), room=sid)

    @socket.on('leave')
    def on_leave_room(data):
        sid = data['session_id']
        cid = data['client_id']
        leave_room(sid)
        emit("Client {} left session {}".format(cid, sid), room=sid)

    @socket.on('message')
    def handle_message(message):
        send(message)

    @socket.on('json')
    def handle_json(json):
        sid = json['session_id'] if 'session_id' in json else request.sid
        send(json, json=True, room=sid)
