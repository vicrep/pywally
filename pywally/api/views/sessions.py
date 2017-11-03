import logging

from flask_restplus import Resource

from pywally.api import api, models

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
        pass

    @api.response(201, 'Session successfully created.')
    @api.expect(models.session_create_req)
    def post(self):
        """Create a new session"""
        log.debug('Creating new session')
        pass


@ns.route('/<string:id>')
@api.response(404, 'Post not found.')
class Session(Resource):
    @api.marshal_with(models.session)
    def get(self, id):
        """Get a session object"""
        log.debug('Requested session (id:%s)', id)
        pass
