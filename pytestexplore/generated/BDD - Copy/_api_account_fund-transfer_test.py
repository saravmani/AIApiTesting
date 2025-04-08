import pytest
import requests
import time

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

# Helper function to login and return the bearer token
def login_and_get_token():
    login_data = {
        "identifier": "genai_test_user@example.com",
        "password": "Secure#1234"
    }
    response = requests.post(f"{BASE_URL}/api/users/login", json=login_data)
    return response.json().get('token')

@pytest.fixture
def valid_token():
    return login_and_get_token()

@pytest.fixture
def headers(valid_token):
    return {"Authorization": f"Bearer {valid_token}"}

def test_successful_fund_transfer(headers):
    data = {
        "sourceAccountNumber": "856899",
        "targetAccountNumber": "exactly",
        "amount": 200.00,
        "pin": "artist"
    }
    response = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

def test_fund_transfer_with_invalid_pin(headers):
    data = {
        "sourceAccountNumber": "856899",
        "targetAccountNumber": "exactly",
        "amount": 200.00,
        "pin": "wrong-pin"
    }
    response = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_fund_transfer_amount_not_multiple_of_100(headers):
    data = {
        "sourceAccountNumber": "856899",
        "targetAccountNumber": "exactly",
        "amount": 50.00,
        "pin": "artist"
    }
    response = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_fund_transfer_without_valid_authentication():
    data = {
        "sourceAccountNumber": "856899",
        "targetAccountNumber": "exactly",
        "amount": 200.00,
        "pin": "artist"
    }
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)

def test_repeated_fund_transfer_to_check_duplicate_transactions(headers):
    data = {
        "sourceAccountNumber": "856899",
        "targetAccountNumber": "exactly",
        "amount": 200.00,
        "pin": "artist"
    }
    response1 = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    response2 = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    assert response1.status_code == 200
    assert response2.status_code == 200
    time.sleep(DELAY_SECONDS)

def test_fund_transfer_with_insufficient_funds(headers):
    data = {
        "sourceAccountNumber": "856899",
        "targetAccountNumber": "exactly",
        "amount": 1000000.00,
        "pin": "artist"
    }
    response = requests.post(f"{BASE_URL}/api/account/fund-transfer", json=data, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)
