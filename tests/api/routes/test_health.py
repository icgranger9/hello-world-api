

class TestHealthRouter:
    """Grouped tests for the `/api/health` router."""


    def test_health(self, client):
        r = client.get("/api/health/")
        assert r.status_code == 200
        assert r.json() == {"status": "healthy"}
