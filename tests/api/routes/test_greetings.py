

class TestGreetingsRouter:
    """Grouped tests for the `/api/greetings` router."""


    def test_greetings(self, client):
        r = client.get("/api/greetings/")
        assert r.status_code == 200
        assert r.json() == {"message": "Hello from the greetings route!"}

    def test_personalized_greeting(self, client):
        r = client.get("/api/greetings/Ian")
        assert r.status_code == 200
        assert r.json() == {"message": "Hello, Ian!"}
