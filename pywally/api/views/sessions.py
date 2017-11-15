import logging

from flask_restplus import Resource

from pywally.api import api, models
from pywally.api.session_state import DAO as session_state

log = logging.getLogger(__name__)

ns = api.namespace(
    'sessions',
    description='Operations related to Session management'
)


@ns.route('/')
class SessionsCollection(Resource):
    @api.marshal_with(models.session_list)
    def get(self):
        """Get list of existing sessions"""
        log.debug('Requested list of sessions')
        sessions = session_state.get_all_sessions()
        return {
            'count': len(sessions),
            'sessions': sessions,
        }

    @api.marshal_with(
        models.session_info,
        code=201,
        description='Session successfully created.'
    )
    @api.expect(models.session_create_req)
    def post(self):
        """Create a new session"""
        log.debug('Creating new session')
        req = api.payload
        session = session_state.create(**req)
        return session, 201


@ns.route('/<string:id>')
class Session(Resource):
    @api.marshal_with(models.session)
    def get(self, id):
        """Get a session object"""
        log.debug('Requested session %s', id)
        return session_state.get_session(id)

    def delete(self, id):
        log.debug('Requested delete of session %s', id)
        return session_state.delete(id), 204
