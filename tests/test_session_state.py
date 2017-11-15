import pytest


def assert_uuid(id: str):
    """assert that a a provided id is a valid UUIDv1"""
    import uuid
    try:
        uuid.UUID(id, version=1)
    except KeyError:
        pytest.fail('ID provided not a valid UUID v1')


def test_create_session(
    session_state
):
    session = session_state.create()
    assert_uuid(session['id'])
    assert session_state.sessions[session['id']] == session
    assert session['name'] == ''
    assert session['observer'] is None
    assert session['publishers'] == []


def test_create_session_with_name(
    session_state
):
    session = session_state.create('test name')
    assert_uuid(session['id'])
    assert session_state.sessions[session['id']] == session
    assert session['name'] == 'test name'
    assert session['observer'] is None
    assert session['publishers'] == []


def test_get_session(
    session_state_with_sessions,
    session_with_name
):
    sid = session_with_name['id']
    result = session_state_with_sessions.get_session(sid)
    assert result == session_with_name


def test_get_non_existent_session_returns_none(
    session_state
):
    session = session_state.get_session('a_non_existent_session')
    assert session is None


def test_delete_session(
    session_state_with_sessions,
    session_with_name
):
    assert session_state_with_sessions.delete(
        session_with_name['id']
    ) is True


def test_delete_non_existent_session_returns_false(
    session_state,
):
    assert session_state.delete(
        'random_session'
    ) is False


def test_get_sessions(
    session_state_with_sessions,
    session_with_name,
    session_without_name
):
    sessions = session_state_with_sessions.get_all_sessions()
    assert len(sessions) == 2
    assert session_with_name in sessions
    assert session_without_name in sessions
