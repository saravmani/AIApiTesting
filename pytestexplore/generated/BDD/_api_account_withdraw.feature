Feature: Cash Withdrawal

  Background:
    Given a user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"
    And the user has a valid Bearer token

  Scenario: Successful withdrawal
    Given the user's account balance is sufficient
    And the amount is a multiple of 100
    When the user requests to withdraw an amount of 500
    Then the withdrawal should be successful
    And the API should return a 200 status code
    And a success message indicating the withdrawal was successful

  Scenario: Withdrawal amount not a multiple of 100
    Given the user's account balance is sufficient
    When the user requests to withdraw an amount of 931.24
    Then the withdrawal should fail
    And the API should return an error message stating the amount must be a multiple of 100

  Scenario: Insufficient account balance
    Given the user's account balance is less than the withdrawal amount
    When the user requests to withdraw an amount of 5000
    Then the withdrawal should fail
    And the API should return an error message indicating insufficient funds

  Scenario: Invalid authentication token
    Given the user has an invalid Bearer token
    When the user requests to withdraw an amount of 500
    Then the request should be unauthorized
    And the API should return a 401 status code

  Scenario: Invalid PIN
    Given the user provides an incorrect PIN
    When the user requests to withdraw an amount of 500
    Then the withdrawal should fail
    And the API should return an error message indicating invalid PIN