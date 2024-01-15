import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture()
def client():
    return TestClient(app)


class TestMain:
    def test_root_redirect(self, client: TestClient):
        response = client.get("/", follow_redirects=False)
        assert response.status_code == 307

        response = client.get("/", follow_redirects=True)
        assert response.status_code == 200
        assert response.url == client.base_url.join("/api/docs")
