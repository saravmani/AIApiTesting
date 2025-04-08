Feature: User Profile Update

  Background:
    Given a user is registered with the following details:
      | id   | name  | password    | email                  | countryCode | phoneNumber | address         |
      | 813  | truth | 2^RX(BFm^E  | genai_test_user@example.com | member     | class       | activity         |
    And a bearer token is obtained for the user

  Scenario: Successfully update user profile
    Given the user is authenticated with a valid bearer token
    When the user updates their profile with the following data:
      | id   | name     | password    | email                  | countryCode | phoneNumber | address               |
      | 813  | honesty  | NewPass#123 | genai_test_user@example.com | member     | newClass    | new activity |
    Then the response should indicate success

  Scenario: Update user profile with an invalid token
    Given the user is authenticated with an invalid bearer token
    When the user attempts to update their profile
    Then the update should fail with an authentication error

  Scenario: Update user profile with the same email
    Given the user is authenticated with a valid bearer token
    When the user updates their profile with a duplicate email:
      | email                  |
      | genai_test_user@example.com |
    Then the update should fail with a duplicate email error

  Scenario: Update user profile with the same phone number
    Given the user is authenticated with a valid bearer token
    When the user updates their profile with a duplicate phone number:
      | phoneNumber |
      | class        |
    Then the update should fail with a duplicate phone number error

