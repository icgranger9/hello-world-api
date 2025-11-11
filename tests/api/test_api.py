

class TestAPIRouter:
    """Tests for the `/api` router and its registered sub-routers."""

    def test_api_root(self, client):
        r = client.get("/api/")
        assert r.status_code == 200
        assert r.json() == {"message": "Hello from the api route!"}
    
