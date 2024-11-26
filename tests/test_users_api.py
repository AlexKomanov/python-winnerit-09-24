import requests
import pytest
from assertpy import assert_that

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def test_get_all_users():
    response = requests.get(BASE_URL)
    assert_that(response.status_code).is_equal_to(200)
    users = response.json()
    assert_that(users).is_not_empty()
    assert_that(len(users)).is_equal_to(10)

def test_get_user_by_id():
    user_id = 1
    response = requests.get(f"{BASE_URL}/{user_id}")
    assert_that(response.status_code).is_equal_to(200)
    user = response.json()
    assert_that(user).has_name("Leanne Graham")
    assert_that(user).has_email("Sincere@april.biz")

def test_user_not_found():
    user_id = 999
    response = requests.get(f"{BASE_URL}/{user_id}")
    assert_that(response.status_code).is_equal_to(404)

def test_user_structure():
    user_id = 2
    response = requests.get(f"{BASE_URL}/{user_id}")
    user = response.json()
    assert_that(user).has_id(2)
    assert_that(user).has_username("Antonette")
    assert_that(user["address"]).has_city("Wisokyburgh")
    assert_that(user["company"]).has_name("Deckow-Crist")

@pytest.mark.parametrize("user_id, expected_name", [
    (3, "Clementine Bauch"),
    (4, "Patricia Lebsack"),
    (5, "Chelsey Dietrich")
])
def test_multiple_users(user_id, expected_name):
    response = requests.get(f"{BASE_URL}/{user_id}")
    user = response.json()
    assert_that(user).has_name(expected_name)