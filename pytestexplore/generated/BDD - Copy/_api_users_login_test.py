import pytest
import requests
import time
from pytest_bdd import given

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

@given("test successful login")
def test_successful_login():
    payload = {"identifier": "genai_test_user@example.com", "password": "Secure#1234"}
    response = requests.post(f"{BASE_URL}/api/users/login", json=payload)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

@given("test unsuccessful login with invalid password")
def test_unsuccessful_login_invalid_password():
    payload = {"identifier": "genai_test_user@example.com", "password": "invalidPass1!"}
    response = requests.post(f"{BASE_URL}/api/users/login", json=payload)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)

@given("test unsuccessful login with invalid identifier")
def test_unsuccessful_login_invalid_identifier():
    payload = {"identifier": "wrong_user@example.com", "password": "Secure#1234"}
    response = requests.post(f"{BASE_URL}/api/users/login", json=payload)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)

@given("test unsuccessful login with empty credentials")
def test_unsuccessful_login_empty_credentials():
    payload = {"identifier": "", "password": ""}
    response = requests.post(f"{BASE_URL}/api/users/login", json=payload)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)