import pytest
from starlette.testclient import TestClient

from app.main import v1


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(v1)
    yield client  # testing happens here
