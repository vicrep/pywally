import pytest
from pywally import main


@pytest.fixture
def app():
    app = main.create_app()
    app.debug = True
    return app.test_client()
