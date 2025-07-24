import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_stats_known_short_code(client):
    url = "http://www.thisismyverylongdomainnamethatisreallyreallylong.com/"
    response = client.post('/api/shorten', json={"url": url})
    short_code = response.json['short_code']
    stats_response = client.get(f"/api/stats/{short_code}")
    assert stats_response.status_code == 200
    assert stats_response.json["clicks"] == 0
    assert stats_response.json["url"] == url



def test_stats_unknown_code(client):
    response = client.get("/api/stats/try123")
    assert response.status_code == 404
