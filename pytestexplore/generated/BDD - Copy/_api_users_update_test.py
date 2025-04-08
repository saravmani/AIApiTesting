import pytest
import requests
import time

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"
LOGIN_URL = f"{BASE_URL}/api/users/login"
UPDATE_URL = f"{BASE_URL}/api/users/update"

# Sample credentials, token should be retrieved dynamically
USER_CREDENTIALS = {
    "identifier": "genai_test_user@example.com",
    "password": "Secure#1234"
}

def get_bearer_token():
    response = requests.post(LOGIN_URL, json=USER_CREDENTIALS)
    return response.json().get("token")

@pytest.fixture
def headers_with_auth():
    bearer_token = get_bearer_token()
    return {"Authorization": f"Bearer {bearer_token}"}

def test_successfully_update_user_profile(headers_with_auth):
    data = {
        "id": 251,
        "name": "change",
        "password": "#1Yl5ZLBxE",
        "email": "important",
        "countryCode": "agreement",
        "phoneNumber": "beautiful",
        "address": "save"
    }
    response = requests.post(UPDATE_URL, headers=headers_with_auth, json=data)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

def test_update_user_profile_with_missing_name(headers_with_auth):
    data = {
        "id": 251,
        "name": "",
        "password": "#1Yl5ZLBxE",
        "email": "important",
        "countryCode": "agreement",
        "phoneNumber": "beautiful",
        "address": "save"
    }
    response = requests.post(UPDATE_URL, headers=headers_with_auth, json=data)
    assert response.status_code == 400  # Assuming 400 for bad request
    time.sleep(DELAY_SECONDS)

def test_update_user_profile_with_invalid_email_format(headers_with_auth):
    data = {
        "id": 251,
        "name": "change",
        "password": "#1Yl5ZLBxE",
        "email": "not_an_email",
        "countryCode": "agreement",
        "phoneNumber": "beautiful",
        "address": "save"
    }
    response = requests.post(UPDATE_URL, headers=headers_with_auth, json=data)
    assert response.status_code == 400  # Assuming 400 for bad request
    time.sleep(DELAY_SECONDS)

def test_failed_update_due_to_missing_authentication_token():
    data = {
        "id": 251,
        "name": "change",
        "password": "#1Yl5ZLBxE",
        "email": "important",
        "countryCode": "agreement",
        "phoneNumber": "beautiful",
        "address": "save"
    }
    response = requests.post(UPDATE_URL, json=data)
    assert response.status_code == 401
    time.sleep(DELAY_SECONDS)