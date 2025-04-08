Feature: Create PIN

  Background:
    Given a user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"

  Scenario: Successfully create a new PIN
    Given the account with accountNumber 856899 exists
    When the user creates a PIN with "1234" for the account
    Then the response status code should be 200
    And the response should indicate PIN creation success

  Scenario: Attempt to create a duplicate PIN
    Given the account with accountNumber 856899 already has a PIN set as "1234"
    When the user tries to create a duplicate PIN "1234" for the account
    Then the response status code should be an error code (like 409)
    And the response should indicate the PIN already exists

  Scenario: Fail to create a PIN with missing accountNumber
    When the user creates a PIN with "" for the account
    Then the response status code should be an error code (like 400)
    And the response should indicate missing account information

  Scenario: Fail to create a PIN with invalid authentication
    Given the user tries to create a PIN without a valid authentication token
    When the user creates a PIN with "1234" for the account
    Then the response status code should be 401
    And the response should indicate an authentication error
