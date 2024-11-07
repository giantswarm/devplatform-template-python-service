def test_ping(app):
    with app.test_client() as client:
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.data == b"pong"
