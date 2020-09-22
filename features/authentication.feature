# Created by ali at 9/20/20
Feature: Login to FastHub application with basic authentication (username & password)

  @device-AndroidEmulator
  Scenario Outline: Login to account with correct user info then logout
    Given I lunch application
    Then I should see login activity
    When I choose my login type "Basic Authentication"
    When I enter username as <Username> and password as <Password>
    And I click on login button
    Then I should see main menu activity "FastHub"
    When I click on side menu button
    And I click on "Profile" tab
    And I click on "Logout" option
    And I click on "Yes" to confirm logout
    Examples:
      | Username   | Password         |
      | testofcafe | qacafebazaar2020 |
