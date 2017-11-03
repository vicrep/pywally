from flask_restplus import fields

from pywally.api import api


client = api.model('Client', {
    'id': fields.String(required=True),
    'name': fields.String(description='name of the client'),
    'client_type': fields.String(
        required=True,
        enum=['observer', 'publisher']
    )
})

observer = api.inherit('Observer', client, {
    'client_type': fields.String(enum=['observer']),
})

publisher = api.inherit('Publisher', client, {
    'client_type': fields.String(enum=['publisher']),
})

session_info = api.model('Session Info', {
    'id': fields.String(required=True),
    'name': fields.String(description='name of the session'),
})

session = api.clone('Session', session_info, {
    'observer': fields.Nested(
        observer,
        description='''client which takes incoming
        streams and displays them to the user''',
        required=True
    ),
    'publishers': fields.List(
        fields.Nested(publisher),
        description='''clients
        which send video streams, who will be
        received by an observer''',
        required=True
    )
})

session_list = api.model('Session List', {
    'sessions': fields.List(fields.Nested(session_info)),
    'count': fields.Integer(min=0),
})

session_create_req = api.model('New Session Request', {
    'name': fields.String(description='name to give the session'),
})
