Feature: flaskr is secure in that users must log in and out to
  access certain features

  Scenario: successful login
    Given flaskr is set up
    When we log in in with "admin" and "pass"
    Then we should see the alert "You were logged in"

  Scenario: incorrect username
    Given flaskr is set up
    When we log in with "user" and "admin"
    Then we should see the alert "invalid user"

  Scenario: incorrect password
    Given flaskr is set up
    When we log in with "admin" and "something"
    Then we should see and alert "Invalid password"

  Scenario: successful logout
    Given flaskr is set up
    And we log in with with "admin" and "pass"
    When we log out
    Then we should see the alert "You were logged out"