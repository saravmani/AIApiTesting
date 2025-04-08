import pytest
import requests
import time
from pytest_bdd import given

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

def login_get_token():
    login_payload = {
        "identifier": "genai_test_user@example.com",
        "password": "Secure#1234"
    }
    response = requests.post(f"{BASE_URL}/api/users/login", json=login_payload)
    return response.json().get("token")

@given("successful cash deposit")
def test_successful_cash_deposit():
    token = login_get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "accountNumber": 856899,
        "pin": "1234",
        "amount": 500.22
    }
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

@given("deposit with amount greater than 100,000")
def test_deposit_greater_than_100000():
    token = login_get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "accountNumber": 856899,
        "pin": "1234",
        "amount": 100000.1
    }
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("deposit with amount not in multiples of 100")
def test_deposit_not_in_multiples_of_100():
    token = login_get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "accountNumber": 856899,
        "pin": "1234",
        "amount": 150.22
    }
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("deposit with amount less than or equal to 0")
def test_deposit_amount_less_or_equal_zero():
    token = login_get_token()
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "accountNumber": 856899,
        "pin": "1234",
        "amount": 0
    }
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("invalid bearer token during deposit")
def test_invalid_bearer_token_during_deposit():
    headers = {"Authorization": "Bearer invalid_token"}

    payload = {
        "accountNumber": 856899,
        "pin": "1234",
        "amount": 500.22
    }
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)
