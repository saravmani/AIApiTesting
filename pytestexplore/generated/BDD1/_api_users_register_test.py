import pytest
import requests
import time

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

def test_successful_user_registration():
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "password": "Strong#1234",
        "countryCode": "IN",
        "phoneNumber": "912345678901",  # Updated to 12 digits
        "address": "123 Baker Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    assert response.status_code == 200
    time.sleep(DELAY_SECONDS)

def test_registration_fails_due_to_duplicate_phone():
    # First registration for setup
    user_data = {
        "name": "Initial User",
        "email": "initial@example.com",
        "password": "Initial#1234",
        "countryCode": "IN",
        "phoneNumber": "912345678901",  # Updated to 12 digits
        "address": "Initial Baker Street, London"
    }
    requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    # Duplicate phone number registration
    duplicate_user = {
        "name": "Jane Doe",
        "email": "newemail@example.com",
        "password": "Secure#1234",
        "countryCode": "IN",
        "phoneNumber": "912345678901",  # Updated to 12 digits
        "address": "221B Baker Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=duplicate_user)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_registration_fails_due_to_duplicate_email():
    # First registration for setup
    user_data = {
        "name": "Another User",
        "email": "jane.doe@example.com",
        "password": "Another#1234",
        "countryCode": "IN",
        "phoneNumber": "912345678902",
        "address": "Another Baker Street, London"
    }
    requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    # Duplicate email registration
    duplicate_user = {
        "name": "Richard Roe",
        "email": "jane.doe@example.com",
        "password": "Safe&4567",
        "countryCode": "IN",
        "phoneNumber": "912345678902",
        "address": "456 Main Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=duplicate_user)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_registration_fails_due_to_weak_password():
    user_data = {
        "name": "Emma Caller",
        "email": "emma.caller@example.com",
        "password": "weakpass",
        "countryCode": "IN",
        "phoneNumber": "912345678903",
        "address": "789 Elm Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

def test_registration_fails_due_to_invalid_password_policy():
    user_data = {
        "name": "Sam Smith",
        "email": "sam.smith@example.com",
        "password": "abcDE1234",
        "countryCode": "IN",
        "phoneNumber": "912345678904",
        "address": "159 Orchard Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)

# New test case
def test_registration_fails_due_to_invalid_mobile_number():
    user_data = {
        "name": "Alice Joe",
        "email": "alice.joe@example.com",
        "password": "Super#5678",
        "countryCode": "IN",
        "phoneNumber": "98765432",  # Invalid mobile number
        "address": "2461 Baker Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    assert response.status_code == 400
    assert response.text == "In Valid Mobile Number"
    time.sleep(DELAY_SECONDS)