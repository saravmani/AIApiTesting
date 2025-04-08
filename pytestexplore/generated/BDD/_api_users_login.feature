Feature: User Login

  Scenario: Successful login with valid credentials
    Given the user has valid login credentials
      | identifier                     | password    |
      | genai_test_user@example.com    | Secure#1234 |
    When the user attempts to login through the POST /api/users/login endpoint
    Then the API should return a token in the response
    And the status code should be 200

  Scenario: Login with invalid password
    Given the user has invalid login credentials
      | identifier                     | password    |
      | genai_test_user@example.com    | WrongPass   |
    When the user attempts to login through the POST /api/users/login endpoint
    Then the API should return an authentication error
    And the status code should be 401

  Scenario: Login with non-existent user
    Given the user does not exist
      | identifier                     | password    |
      | non_existent_user@example.com  | Secure#1234 |
    When the user attempts to login through the POST /api/users/login endpoint
    Then the API should return an error indicating user not found
    And the status code should be 404

  Scenario: Login without providing identifier
    Given the user input lacks identifier
      | password    |
      | Secure#1234 |
    When the user attempts to login through the POST /api/users/login endpoint
    Then the API should return a validation error
    And the status code should be 400

  Scenario: Login without providing password
    Given the user input lacks password
      | identifier                     |
      | genai_test_user@example.com    |
    When the user attempts to login through the POST /api/users/login endpoint
    Then the API should return a validation error
    And the status code should be 400
