Feature: User Login

  Scenario: Successful login
    Given the user has valid credentials
      | identifier                  | password     |
      | genai_test_user@example.com | Secure#1234  |
    When the user sends a POST request to "/api/users/login"
    Then the response should have status code 200
    And the response body should contain a token

  Scenario: Unsuccessful login with invalid password
    Given the user has invalid credentials
      | identifier                  | password      |
      | genai_test_user@example.com | invalidPass1! |
    When the user sends a POST request to "/api/users/login"
    Then the response should have status code 401
    And the response body should not contain a token

  Scenario: Unsuccessful login with invalid identifier
    Given the user has invalid credentials
      | identifier      | password     |
      | wrong_user@example.com | Secure#1234  |
    When the user sends a POST request to "/api/users/login"
    Then the response should have status code 401
    And the response body should not contain a token

  Scenario: Unsuccessful login with empty credentials
    Given the user has empty credentials
      | identifier | password |
      |            |          |
    When the user sends a POST request to "/api/users/login"
    Then the response should have status code 400
    And the response body should not contain a token
