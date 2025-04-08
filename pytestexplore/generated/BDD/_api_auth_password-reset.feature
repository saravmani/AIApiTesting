Feature: Password Reset

  Scenario: Successful password reset
    Given I have a valid identifier "genai_test_user@example.com"
    And I have a new password "Qk4YZZ8qj!"
    When I request a password reset
    Then I should receive a success message

  Scenario: Attempt to reset password with an invalid identifier
    Given I have an invalid identifier "unknown_user@example.com"
    And I have a new password "Qk4YZZ8qj!"
    When I request a password reset
    Then I should receive an error message indicating invalid identifier

  Scenario: Attempt to reset password with invalid password format
    Given I have a valid identifier "genai_test_user@example.com"
    And I have an invalid new password "short"
    When I request a password reset
    Then I should receive a 400 bad request error indicating password policy violation

  Scenario: Attempt to reset password with existing credentials without changes
    Given I have a valid identifier "genai_test_user@example.com"
    And I have a password that matches the existing "Secure#1234"
    When I request a password reset
    Then I should receive a message indicating password unchanged due to duplication

  Scenario: No identifier provided for password reset
    Given I have not provided an identifier
    And I have a new password "Qk4YZZ8qj!"
    When I request a password reset
    Then I should receive an error message indicating missing identifier

  Scenario: No password provided for password reset
    Given I have a valid identifier "genai_test_user@example.com"
    And I have not provided a new password
    When I request a password reset
    Then I should receive an error message indicating missing new password
