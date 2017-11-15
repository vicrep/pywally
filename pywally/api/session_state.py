import uuid

from pywally.api import api


class SessionDAO(object):
    def __init__(self):
        self.sessions = {}

    def create(self, name: str = ''):
        sid = str(uuid.uuid1())
        session = {
            'id': sid,
            'name': name,
            'observer': None,
            'publishers': []
        }
        self.sessions[sid] = session
        return session

    def get_session(self, session_id: str):
        if session_id not in self.sessions:
            api.abort(
                404,
                'No session found with id {}.'.format(session_id)
            )
        else:
            return self.sessions[session_id]

    def get_all_sessions(self):
        return list(self.sessions.values())

    def delete(self, session_id: str):
        if session_id not in self.sessions:
            api.abort(
                404,
                'Cannot delete session {} since it does not exist.'.format(
                    session_id)
            )
        self.sessions.pop(session_id)
        return True


DAO = SessionDAO()
