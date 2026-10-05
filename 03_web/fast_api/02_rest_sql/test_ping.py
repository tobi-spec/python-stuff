def test_ping(test_client):
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}

def test_ping_async(test_client):
    response = test_client.get("/ping/async")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}
