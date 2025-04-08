import pytest
import requests
import time

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"
AUTH_TOKEN = "Bearer <your_auth_token_here>"  # Replace with actual token if available

@pytest.fixture(scope="function")
def auth_header():
    return {'Authorization': AUTH_TOKEN}

# Scenario: Successfully create a new PIN
def test_create_pin_success(auth_header):
    data = {
        "accountNumber": "856899",
        "pin": "1234",
        "password": "Secure#1234"
    }
    response = requests.post(f"{BASE_URL}/api/account/pin/create", json=data, headers=auth_header)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

# Scenario: Attempt to create a duplicate PIN
def test_create_duplicate_pin(auth_header):
    data = {
        "accountNumber": "856899",
        "pin": "1234",
        "password": "Secure#1234"
    }
    # Create first to setup duplicate scenario
    requests.post(f"{BASE_URL}/api/account/pin/create", json=data, headers=auth_header)
    # Attempt to create duplicate
    response = requests.post(f"{BASE_URL}/api/account/pin/create", json=data, headers=auth_header)
    assert response.status_code == 409  # assuming 409 for conflict
    time.sleep(DELAY_SECONDS)

# Scenario: Fail to create a PIN with missing accountNumber
def test_create_pin_missing_account(auth_header):
    data = {
        "accountNumber": "",
        "pin": "1234",
        "password": "Secure#1234"
    }
    response = requests.post(f"{BASE_URL}/api/account/pin/create", json=data, headers=auth_header)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

# Scenario: Fail to create a PIN with invalid authentication
def test_create_pin_invalid_auth():
    data = {
        "accountNumber": "856899",
        "pin": "1234",
        "password": "Secure#1234"
    }
    response = requests.post(f"{BASE_URL}/api/account/pin/create", json=data)  # No auth header
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)
