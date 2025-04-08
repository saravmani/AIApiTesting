import pytest
import requests
import time

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"
API_URL = f"{BASE_URL}/api/account/withdraw"

@pytest.fixture(scope="module")
def auth_token():
    response = requests.post(f"{BASE_URL}/api/users/login", json={
        "identifier": "genai_test_user@example.com",
        "password": "Secure#1234"
    })
    token = response.json().get("token")
    yield token

@pytest.mark.parametrize("amount, expected_status_code", [
    (500, 200),   # Successful withdrawal
    (931.24, 400),  # Withdrawal amount not a multiple of 100
    (5000, 400)  # Insufficient account balance
])
def test_withdraw(auth_token, amount, expected_status_code):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(API_URL, headers=headers, json={
        "accountNumber": "856899",
        "pin": "1234",
        "amount": amount
    })
    assert response.status_code == expected_status_code
    time.sleep(DELAY_SECONDS)

def test_invalid_authentication_token():
    headers = {"Authorization": "Bearer invalidtoken"}
    response = requests.post(API_URL, headers=headers, json={
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 500
    })
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)
