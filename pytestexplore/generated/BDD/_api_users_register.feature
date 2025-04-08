Feature: User Registration

  Background:
    Given the user accounts configuration is prepared

  Scenario: Successful User Registration
    Given a user with valid details
      | name        | email                       | password      | countryCode | phoneNumber | address           |
      | John Smith  | john.smith@example.com      | Passw0rd!     | IN          | 9876543210  | 123 Elm Street    |
    When the user registers using the "/api/users/register" endpoint
    Then the registration response should be successful with status code 200
    And the response JSON should include the user's details except password

  Scenario: Registration with Existing Email
    Given a user with an existing email
      | name        | email                  | password  | countryCode | phoneNumber  | address           |
      | Jane Doe    | existing.email@domain.com | NewPass1! | IN          | 1234567890   | 456 Oak Avenue    |
    And the user is already registered with the email
    When the user registers using the "/api/users/register" endpoint with existing email
    Then the API should return the error message "Email already exists"

  Scenario: Registration with Existing Phone Number
    Given a user with an existing phone number
      | name        | email                   | password       | countryCode | phoneNumber | address           |
      | Mark White  | mark.white@domain.com   | Another2@Pass  | IN          | 9876543210        | 789 Pine Drive    |
    And the user is already registered with the phone number
    When the user registers using the "/api/users/register" endpoint with existing phone number
    Then the API should return the error message "Phone number already exists"

  Scenario: Registration with Invalid Password
    Given a user with an invalid password
      | name        | email                  | password  | countryCode | phoneNumber  | address           |
      | Lucy Blue   | lucy.blue@domain.com   | simple    | IN          | 8765432109   | 321 Maple Road    |
    When the user registers using the "/api/users/register" endpoint
    Then the registration should fail with status code 400

  Scenario: Registration with Invalid Email
    Given a user with an invalid email
      | name        | email       | password   | countryCode | phoneNumber | address           |
      | Jack Green  | invalid.com | Valid1#Pass | IN          | 7654321098  | 987 Cedar Lane    |
    When the user registers using the "/api/users/register" endpoint
    Then the registration should fail with status code 400

  Scenario: Missing Required Fields
    Given a user with missing required fields
      | name        | email         | password    | countryCode | phoneNumber | address                    |
      | Null Fields | null@domain.com | @NullPass1! | null       | null       | No Address Provided |
    When the user registers using the "/api/users/register" endpoint
    Then the registration should fail with status code 400
