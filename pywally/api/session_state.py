import uuid


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
        return self.sessions.get(session_id)

    def get_all_sessions(self):
        return list(self.sessions.values())

    def delete(self, session_id: str):
        if session_id not in self.sessions:
            return False
        self.sessions.pop(session_id)
        return True


DAO = SessionDAO()
