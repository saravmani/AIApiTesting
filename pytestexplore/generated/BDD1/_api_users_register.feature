Feature: User Registration

Scenario: Successfully register a new user
  Given a new user with valid details
    | name        | email                           | password    | countryCode | phoneNumber     | address                       |
    | John Doe    | john.doe@example.com            | Strong#1234 | IN          | 912345678901    | 123 Baker Street, London      |
  When the user sends a registration request
  Then the API should return 200 status code
  And the response should include IFSC code, branch, account type, and all input parameters except password

Scenario: Registration fails due to duplicate phone number
  Given a user with a registered phone number
    | name        | email                           | password    | countryCode | phoneNumber | address                    |
    | Jane Doe    | newemail@example.com            | Secure#1234 | IN          | 912345678901  | 221B Baker Street, London |
  When the user sends a registration request
  Then the API should return an error message "Phone number already exists"

Scenario: Registration fails due to duplicate email
  Given a user with a registered email address
    | name        | email                           | password    | countryCode | phoneNumber     | address                    |
    | Richard Roe | jane.doe@example.com            | Safe&4567   | IN          | 912345678902    | 456 Main Street, London    |
  When the user sends a registration request
  Then the API should return an error message "Email already exists"

Scenario: Registration fails due to weak password
  Given a new user with a weak password
    | name        | email                           | password | countryCode | phoneNumber     | address                    |
    | Emma Caller | emma.caller@example.com         | weakpass | IN          | 912345678903    | 789 Elm Street, London     |
  When the user sends a registration request
  Then the API should return 400 status code

Scenario: Registration fails due to invalid password policy
  Given a new user with an invalid password
    | name       | email                            | password   | countryCode | phoneNumber     | address                   |
    | Sam Smith  | sam.smith@example.com            | abcDE1234  | IN          | 912345678904    | 159 Orchard Street, London|
  When the user sends a registration request
  Then the API should return 400 status code and indicates password policy error

Scenario: Registration fails due to invalid mobile number
  Given a new user with an invalid mobile number
    | name      | email                            | password   | countryCode | phoneNumber  | address                       |
    | Alice Joe | alice.joe@example.com            | Super#5678 | IN          | 98765432     | 2461 Baker Street, London    |
  When the user sends a registration request
  Then the API should return 400 status code
  And the response should be "In Valid Mobile Number"
