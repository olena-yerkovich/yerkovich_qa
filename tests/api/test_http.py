import pytest
import requests


base_url = "https://api.github.com"


@pytest.mark.http
def test_first_request():
    r = requests.get(base_url + '/zen')
    print(f"Response is {r.text}")

@pytest.mark.http
def test_second_request():
    r = requests.get(base_url + '/users/defunkt')
    body =  r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get(base_url + '/users/sergii_butenko')

    assert r.status_code == 404
    

   
