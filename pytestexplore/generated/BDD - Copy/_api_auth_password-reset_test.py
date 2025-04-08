import pytest
import requests
import time
from pytest_bdd import given, when, then

DELAY_SECONDS = 1
BASE_URL = "http://localhost:8080"

@given("a user exists with identifier 'genai_test_user@example.com'")
def user_exists():
    # Assume the user is pre-created in the system
    pass

@given("a user does not exist with identifier 'non_existent_user@example.com'")
def user_does_not_exist():
    # No operation needed, assume user does not exist
    pass

@given("a random user identifier 'random_user@example.com'")
def random_user_identifier():
    # Assume no authentication is required for this user
    pass

@when("the user resets the password with new password '_6zEZwnnQk'")
def reset_password():
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json={"identifier": "genai_test_user@example.com", "newPassword": "_6zEZwnnQk"})
    time.sleep(DELAY_SECONDS)
    return response

@when("the user attempts to reset the password with new password '_6zEZwnnQk'")
def attempt_reset_password():
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json={"identifier": "non_existent_user@example.com", "newPassword": "_6zEZwnnQk"})
    time.sleep(DELAY_SECONDS)
    return response

@when("the user resets the password with a weak new password 'weakpass'")
def reset_weak_password():
    response = requests.post(f"{BASE_URL}/api/auth/password-reset", json={"identifier": "genai_test_user@example.com", "newPassword": "weakpass"})
    time.sleep(DELAY_SECONDS)
    return response

@then("the system should respond with a success message")
def verify_success(reset_password):
    assert reset_password.status_code == 200

@then("the system should respond with a failure message indicating user not found")
def verify_user_not_found(attempt_reset_password):
    assert attempt_reset_password.status_code == 404  # Assuming 404 for user not found

@then("the system should respond with a failure message indicating password policy violation")
def verify_password_policy_violation(reset_weak_password):
    assert reset_weak_password.status_code == 400  # Assuming 400 for password policy violation

@then("the action should be performed without requiring authentication")
def verify_no_auth_required(reset_password):
    assert reset_password.status_code == 200
