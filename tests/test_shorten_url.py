import pytest
from app.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_shorten_valid_url(client):
    long_url = "http://www.thisismyverylongdomainnamethatisreallyreallylong.com/"
    response = client.post('/api/shorten', json={"url": long_url})
    assert response.status_code == 200
    assert "short_code" in response.json
    assert "shortened_url" in response.json

def test_shorten_invalid_url(client):
    invalid_url = "http:/example.com"
    response = client.post('/api/shorten', json= {"url": invalid_url})
    assert response.status_code == 400
    assert 'Invalid Url' in response.json['error']


def test_shorten_missing_url(client):
    response = client.post('/api/shorten', json={})
    assert response.status_code == 404
    assert 'Missing Url' in response.json['error']


def test_same_url_shortening( client):
    sample_url = "http://www.thisismyverylongdomainnamethatisreallyreallylong.com/"
    response1 = client.post('/api/shorten',json={'url': sample_url})
    assert response1.status_code == 200
    data1 = response1.get_json()

    response2 = client.post('/api/shorten',json={'url': sample_url})
    assert response2.status_code == 200
    data2 = response2.get_json()
    assert data1['short_code'] == data2['short_code']
    assert data1['shortened_url'] == data2['shortened_url']

