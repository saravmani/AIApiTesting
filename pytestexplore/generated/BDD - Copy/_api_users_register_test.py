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
        "phoneNumber": "9876543210",
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
        "phoneNumber": "9876543210",
        "address": "Initial Baker Street, London"
    }
    requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    # Duplicate phone number registration
    duplicate_user = {
        "name": "Jane Doe",
        "email": "newemail@example.com",
        "password": "Secure#1234",
        "countryCode": "IN",
        "phoneNumber": "9876543210",
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
        "phoneNumber": "9876543219",
        "address": "Another Baker Street, London"
    }
    requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    # Duplicate email registration
    duplicate_user = {
        "name": "Richard Roe",
        "email": "jane.doe@example.com",
        "password": "Safe&4567",
        "countryCode": "IN",
        "phoneNumber": "9876543219",
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
        "phoneNumber": "9876543220",
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
        "phoneNumber": "9876543221",
        "address": "159 Orchard Street, London"
    }
    response = requests.post(f"{BASE_URL}/api/users/register", json=user_data)
    assert response.status_code == 400
    time.sleep(DELAY_SECONDS)
