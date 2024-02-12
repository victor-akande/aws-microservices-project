from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wikipedia API. Call /summary or /search or /phrases"
    }


def test_read_phrase():
    response = client.get("/phrases/Jesus%20Christ")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "jesus",
            "bc",
            "ad",
            "jesus christ",
            "jesus",
            "nazareth",
            "jewish preacher",
            "religious leader",
        ]
    }
