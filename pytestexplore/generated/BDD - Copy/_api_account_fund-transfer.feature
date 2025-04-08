Feature: Fund Transfer

  Background:
    Given I am logged in with the identifier "genai_test_user@example.com" and password "Secure#1234"
    And I have a valid bearer token

  Scenario: Successful fund transfer
    Given I have an account with account number "856899" and pin "artist"
    When I transfer an amount of 200.00 to the account with account number "exactly"
    Then I should receive a success message of the fund transfer

  Scenario: Fund transfer with invalid PIN
    Given I have an account with account number "856899" and pin "wrong-pin"
    When I transfer an amount of 200.00 to the account with account number "exactly"
    Then I should receive an error message indicating invalid PIN

  Scenario: Fund transfer amount not multiple of 100
    Given I have an account with account number "856899" and pin "artist"
    When I transfer an amount of 50.00 to the account with account number "exactly"
    Then I should receive an error message indicating amount must be in multiples of 100

  Scenario: Fund transfer without valid authentication
    Given I do not have a valid bearer token
    When I transfer an amount of 200.00 to the account with account number "exactly"
    Then I should receive an unauthorized error message

  Scenario: Repeated fund transfer to check duplicate transactions
    Given I have an account with account number "856899" and pin "artist"
    When I transfer an amount of 200.00 to the account with account number "exactly" twice
    Then I should verify that both transactions are processed independently without error

  Scenario: Fund transfer with insufficient funds
    Given I have an account with account number "856899" and pin "artist"
    When I transfer an amount of 1000000.00 to an account with account number "exactly"
    Then I should receive an error message indicating insufficient funds
