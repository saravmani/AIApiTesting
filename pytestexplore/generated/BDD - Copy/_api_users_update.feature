Feature: User Update API

  Background:
    Given the user is authenticated with identifier "genai_test_user@example.com" and password "Secure#1234"

  Scenario: Successfully update user profile
    Given I have a valid bearer token
    When I send a POST request to "/api/users/update" with the following details:
      | id       | name   | password      | email      | countryCode | phoneNumber | address   |
      | 251      | change | #1Yl5ZLBxE    | important  | agreement   | beautiful   | save      |
    Then I should receive a successful response

  Scenario: Update user profile with missing name
    Given I have a valid bearer token
    When I send a POST request to "/api/users/update" with the following details:
      | id       | name | password      | email      | countryCode | phoneNumber | address   |
      | 251      |      | #1Yl5ZLBxE    | important  | agreement   | beautiful   | save      |
    Then I should receive a response indicating the name is required

  Scenario: Update user profile with invalid email format
    Given I have a valid bearer token
    When I send a POST request to "/api/users/update" with the following details:
      | id       | name   | password      | email            | countryCode | phoneNumber | address   |
      | 251      | change | #1Yl5ZLBxE    | not_an_email     | agreement   | beautiful   | save      |
    Then I should receive a response indicating the email format is invalid

  Scenario: Failed update due to missing authentication token
    When I send a POST request to "/api/users/update" with the following details without an authentication token:
      | id       | name   | password      | email      | countryCode | phoneNumber | address   |
      | 251      | change | #1Yl5ZLBxE    | important  | agreement   | beautiful   | save      |
    Then I should receive a 401 Unauthorized error
