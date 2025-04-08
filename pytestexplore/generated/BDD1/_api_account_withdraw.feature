Feature: Cash Withdrawal API Tests

  Background:
    Given I am logged into the system with identifier "genai_test_user@example.com" and password "Secure#1234"
    And I have a valid Bearer token

  Scenario: Successful withdrawal with valid details
    Given I have a valid account with accountNumber "856899"
    And my PIN number is "1234"
    When I request to withdraw an amount of 400
    Then I should receive a success message
    And my status code should be 200

  Scenario: Withdrawal with invalid PIN
    Given I have a valid account with accountNumber "856899"
    And my PIN number is "0000"
    When I request to withdraw an amount of 400
    Then I should receive a failure message
    And my status code should be 401

  Scenario: Withdrawal with invalid Bearer token
    Given I have a valid account with accountNumber "856899"
    And my PIN number is "1234"
    And I do not have a valid Bearer token
    When I request to withdraw an amount of 400
    Then I should receive an authentication failure message
    And my status code should be 401

  Scenario: Withdrawal with amount not in multiples of 100
    Given I have a valid account with accountNumber "856899"
    And my PIN number is "1234"
    When I request to withdraw an amount of 489
    Then I should receive a failure message
    And my status code should be 400

  Scenario: Withdrawal with amount greater than account balance
    Given I have a valid account with accountNumber "856899"
    And my PIN number is "1234"
    When I request to withdraw an amount of 1000000
    Then I should receive a failure message
    And my status code should be 400