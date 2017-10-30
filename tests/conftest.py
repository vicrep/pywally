import pytest
import pywally


@pytest.fixture
def app():
    app = pywally.app
    app.debug = True
    return app.test_client()
