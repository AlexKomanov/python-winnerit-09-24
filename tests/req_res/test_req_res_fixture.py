import pytest
import requests

@pytest.fixture
def base_url():
    return 'https://reqres.in/api'

def test_get_user(base_url):
    response = requests.get(f'{base_url}/users/2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2

def test_create_user(base_url):
    new_user = {"name": "John Doe", "job": "Developer"}
    response = requests.post(f'{base_url}/users', json=new_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['name'] == "John Doe"

def test_update_user(base_url):
    update_user = {"name": "Jane Doe", "job": "Manager"}
    response = requests.put(f'{base_url}/users/2', json=update_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 200
    assert response.json()['name'] == "Jane Doe"
    assert response.json()['job'] == "Manager"

def test_delete_user(base_url):
    response = requests.delete(f'{base_url}/users/2')
    print(response.status_code)
    print(response.reason)
    assert response.status_code == 204