Feature: Cash Deposit to Account

  Background:
    Given a valid user with account number "856899"
    And a user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"
    And a valid Bearer token is obtained

  Scenario: Successful cash deposit
    Given the deposit request payload is
      """
      {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 200
      }
      """
    When the user calls POST /api/account/deposit with the Bearer token
    Then the response status should be 200
    And the money is deposited to the account

  Scenario: Deposit with amount greater than 100,000
    Given the deposit request payload is
      """
      {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 100001
      }
      """
    When the user calls POST /api/account/deposit with the Bearer token
    Then the response status should be 400
    And the response contains error message "Amount cannot be greater than 100,000"

  Scenario: Deposit with amount not in multiples of 100
    Given the deposit request payload is
      """
      {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 550
      }
      """
    When the user calls POST /api/account/deposit with the Bearer token
    Then the response status should be 400
    And the response contains error message "Amount must be in multiples of 100"

  Scenario: Deposit with zero amount
    Given the deposit request payload is
      """
      {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 0
      }
      """
    When the user calls POST /api/account/deposit with the Bearer token
    Then the response status should be 400
    And the response contains error message "Amount must be greater than 0"

  Scenario: Deposit with invalid amount
    Given the deposit request payload is
      """
      {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": -500
      }
      """
    When the user calls POST /api/account/deposit with the Bearer token
    Then the response status should be 400
    And the response contains error message "Invalid amount"

  Scenario: Unauthorized deposit due to invalid token
    Given the deposit request payload is
      """
      {
        "accountNumber": "856899",
        "pin": "1234",
        "amount": 900
      }
      """
    And an invalid bearer token
    When the user calls POST /api/account/deposit with the invalid Bearer token
    Then the response status should be 401
    And the response contains error message "Invalid authentication token"
