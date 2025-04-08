Feature: Cash Deposit API

  Scenario: Successful cash deposit
    Given the user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"
    And a valid bearer token is obtained
    When the user makes a POST request to "/api/account/deposit" with payload:
      | accountNumber | pin  | amount |
      | 856899        | 1234 | 100000 |
    Then the response status code should be 200
    And the amount should be deposited successfully

  Scenario: Deposit with amount greater than 200,000
    Given the user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"
    And a valid bearer token is obtained
    When the user makes a POST request to "/api/account/deposit" with payload:
      | accountNumber | pin  | amount    |
      | 856899        | 1234 | 200000.1  |
    Then the response should return an error message "Invalid amount"

  Scenario: Deposit with amount not in multiples of 100
    Given the user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"
    And a valid bearer token is obtained
    When the user makes a POST request to "/api/account/deposit" with payload:
      | accountNumber | pin  | amount |
      | 856899        | 1234 | 150.22 |
    Then the response should return an error message "Invalid amount"

  Scenario: Deposit with amount less than or equal to 0
    Given the user is logged in with identifier "genai_test_user@example.com" and password "Secure#1234"
    And a valid bearer token is obtained
    When the user makes a POST request to "/api/account/deposit" with payload:
      | accountNumber | pin  | amount |
      | 856899        | 1234 | 0      |
    Then the response should return an error message "Invalid amount"

  Scenario: Invalid bearer token during deposit
    Given the user attempts to deposit without logging in
    When the user makes a POST request to "/api/account/deposit" with payload:
      | accountNumber | pin  | amount |
      | 856899        | 1234 | 500.22 |
    Then the response status code should be 401
    And the response should contain an error message "Unauthorized"
