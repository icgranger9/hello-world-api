

class TestMainApp:
    """Tests for the top-level application (root route)."""

    def test_app_root(self, client):
        r = client.get("/")
        assert r.status_code == 200
        assert r.json() == {"message": "Hello from the app route!"}
