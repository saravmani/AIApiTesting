import pytest
import requests
import time
from pytest_bdd import given

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"
VALID_USER = {
    "identifier": "genai_test_user@example.com",
    "password": "Secure#1234",
    "accountNumber": "856899",
    "pin": "1234"
}

def get_bearer_token():
    response = requests.post(f"{BASE_URL}/api/users/login", json={
        "identifier": VALID_USER["identifier"],
        "password": VALID_USER["password"]
    })
    return response.json().get("token")

token = get_bearer_token()

@given("Successful cash deposit")
def test_successful_cash_deposit():
    payload = {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 200
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

@given("Deposit with amount greater than 100,000")
def test_deposit_amount_greater_than_100k():
    payload = {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 100001
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("Deposit with amount not in multiples of 100")
def test_deposit_amount_not_multiples_of_100():
    payload = {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 550
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("Deposit with zero amount")
def test_deposit_zero_amount():
    payload = {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 0
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("Deposit with invalid amount")
def test_deposit_invalid_amount():
    payload = {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": -500
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("Unauthorized deposit due to invalid token")
def test_unauthorized_deposit_invalid_token():
    payload = {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 900
    }
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.post(f"{BASE_URL}/api/account/deposit", json=payload, headers=headers)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)
