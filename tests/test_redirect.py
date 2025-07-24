import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_redirect_to_long_url(client):
    long_url = "https://www.google.com/"
    response = client.post('/api/shorten', json={"url": long_url})
    short_code = response.json['short_code']
    redirect_response = client.get(f"/{short_code}", follow_redirects=False)
    assert redirect_response.status_code == 302
    assert redirect_response.headers['Location'] == long_url

def test_redirect_to_long_url_not_found(client):
    response = client.get('/abs152')
    assert response.status_code == 404
    assert "Not found" in response.json['error']