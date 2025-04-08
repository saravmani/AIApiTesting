Feature: Update Account PIN

  Background:
    Given a user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"

  Scenario: Successfully update account PIN
    Given the user has a valid session token
    When the user attempts to update the PIN with account number "856899", old PIN "1234", new PIN "5678", and password "Secure#1234"
    Then the API should return a success message

  Scenario: Fail to update account PIN due to invalid old PIN
    Given the user has a valid session token
    When the user attempts to update the PIN with account number "856899", old PIN "0000", new PIN "5678", and password "Secure#1234"
    Then the API should return an error message for incorrect old PIN

  Scenario: Fail to update account PIN due to invalid session token
    Given the user has an invalid session token
    When the user attempts to update the PIN with account number "856899", old PIN "1234", new PIN "5678", and password "Secure#1234"
    Then the API should return an authentication error message

  Scenario: Fail to update account PIN without sufficient parameters
    Given the user has a valid session token
    When the user attempts to update the PIN with account number "856899" and password "Secure#1234" only
    Then the API should return a validation error message

  Scenario: Successfully prevent PIN update with duplicate new PIN
    Given the user has a valid session token
    And the new PIN "5678" is already in use for another account
    When the user attempts to update the PIN with account number "856899", old PIN "1234", new PIN "5678", and password "Secure#1234"
    Then the API should return an error message indicating duplicate new PIN
