from pytest import fixture
import pywally


@fixture
def app():
    app = pywally.app
    app.debug = True
    return app.test_client()


@fixture
def session_state():
    from pywally.api.session_state import SessionDAO
    return SessionDAO()


@fixture
def session_without_name():
    session = {
        'id': 'session_with_no_name',
        'name': '',
        'observer': None,
        'publishers': [],
    }
    return session


@fixture
def session_with_name():
    session = {
        'id': 'session_with_name',
        'name': 'test_session',
        'observer': None,
        'publishers': []
    }
    return session


@fixture
def session_state_with_sessions(
    session_state,
    session_with_name,
    session_without_name
):
    session_state.sessions[session_with_name['id']] = session_with_name
    session_state.sessions[session_without_name['id']] = session_without_name
    return session_state
