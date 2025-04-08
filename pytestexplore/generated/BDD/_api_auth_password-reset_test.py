import pytest
import requests
import time
from pytest_bdd import given

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

@given("Successful password reset")
def test_password_reset_successful():
    data = {
        "identifier": "genai_test_user@example.com",
        "newPassword": "Qk4YZZ8qj!"
    }
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json=data)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

@given("Attempt to reset password with an invalid identifier")
def test_password_reset_invalid_identifier():
    data = {
        "identifier": "unknown_user@example.com",
        "newPassword": "Qk4YZZ8qj!"
    }
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json=data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("Attempt to reset password with invalid password format")
def test_password_reset_invalid_password_format():
    data = {
        "identifier": "genai_test_user@example.com",
        "newPassword": "short"
    }
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json=data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("Attempt to reset password with existing credentials without changes")
def test_password_reset_duplicate_password():
    data = {
        "identifier": "genai_test_user@example.com",
        "newPassword": "Secure#1234"
    }
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json=data)
    assert response.status_code == 409
    time.sleep(DELAY_SECONDS)

@given("No identifier provided for password reset")
def test_password_reset_no_identifier():
    data = {
        "newPassword": "Qk4YZZ8qj!"
    }
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json=data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

@given("No password provided for password reset")
def test_password_reset_no_password():
    data = {
        "identifier": "genai_test_user@example.com"
    }
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json=data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)
