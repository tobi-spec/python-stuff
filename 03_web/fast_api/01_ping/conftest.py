import pytest
from starlette.testclient import TestClient
from ping import app

@pytest.fixture(scope='module')
def test_client():
    client = TestClient(app)
    yield client