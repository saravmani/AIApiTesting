Feature: Password Reset

  Scenario: Successfully reset password
    Given a user exists with identifier "genai_test_user@example.com"
    When the user resets the password with new password "_6zEZwnnQk"
    Then the system should respond with a success message

  Scenario: Attempt to reset password with an invalid identifier
    Given a user does not exist with identifier "non_existent_user@example.com"
    When the user attempts to reset the password with new password "_6zEZwnnQk"
    Then the system should respond with a failure message indicating user not found

  Scenario: Attempt to reset password with a weak new password
    Given a user exists with identifier "genai_test_user@example.com"
    When the user resets the password with a weak new password "weakpass"
    Then the system should respond with a failure message indicating password policy violation

  Scenario: Reset password without authentication
    Given a random user identifier "random_user@example.com"
    When the user resets the password with new password "_6zEZwnnQk"
    Then the action should be performed without requiring authentication