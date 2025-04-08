import pytest
import requests
import time

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

@pytest.fixture
def login():
    response = requests.post(f"{BASE_URL}/api/users/login", json={
        "identifier": "genai_test_user@example.com",
        "password": "Secure#1234"
    })
    assert response.status_code == 200
    return response.json()["token"]

def test_update_pin_success(login):
    token = login
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/pin/update", json={
        "accountNumber": "856899",
        "oldPin": "1234",
        "newPin": "5678",
        "password": "Secure#1234"
    }, headers=headers)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

def test_update_pin_invalid_old_pin(login):
    token = login
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/pin/update", json={
        "accountNumber": "856899",
        "oldPin": "0000",
        "newPin": "5678",
        "password": "Secure#1234"
    }, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_update_pin_invalid_session_token():
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.post(f"{BASE_URL}/api/account/pin/update", json={
        "accountNumber": "856899",
        "oldPin": "1234",
        "newPin": "5678",
        "password": "Secure#1234"
    }, headers=headers)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)

def test_update_pin_missing_parameters(login):
    token = login
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/pin/update", json={
        "accountNumber": "856899",
        "password": "Secure#1234"
    }, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_update_pin_duplicate_new_pin(login):
    token = login
    headers = {"Authorization": f"Bearer {token}"}
    # Assume "5678" is already in use
    response = requests.post(f"{BASE_URL}/api/account/pin/update", json={
        "accountNumber": "856899",
        "oldPin": "1234",
        "newPin": "5678",
        "password": "Secure#1234"
    }, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)
