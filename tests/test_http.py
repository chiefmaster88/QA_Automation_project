import pytest
import requests


@pytest.mark.http
def test_first_request():
    req = requests.get('https://api.github.com/zen')
    print(f'Text Request is: {req.text}')
    print(req.status_code)

@pytest.mark.http
def test_second_request():
    req = requests.get('https://api.github.com/users/defunkt')
    body = req.json()
    headers = req.headers
    assert body['name'] == 'Chris Wanstrath'
    assert req.status_code == 200
    assert headers['Server'] == 'GitHub.com'
    print(req.status_code)

@pytest.mark.http
def test_status_code_request():
    req = requests.get('https://api.github.com/users/sergii_butenko ')
    assert req.status_code == 404
    print(req.status_code)