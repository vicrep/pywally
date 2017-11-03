def test_hello_world(app):
    res = app.get("/")
    assert res.status_code == 200
    assert b'Hello, world!' in res.data
