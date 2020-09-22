# Created by ali at 9/20/20
Feature: Create new issue on Cafebazaar Hop project

  @device-AndroidEmulator
  Scenario Outline: Login in to account with correct user info (Basic Authentication method) then search Cafebazaar Hop project and
  Add new issue
    Given I lunch application
    Then I should see login activity
    When I choose my login type "Basic Authentication"
    When I enter username as <Username> and password as <Password>
    And I click on login button
    Then I should see main menu activity "FastHub"
    When I click on search icon
    And I enter <repository_name> in to edit text
    And I click on search icon
    Then I should see repo name <repository_name> in results of search
    When I click <repository_name> from search result
    Then I should see <repository_name> page
    When I click on issue icon
    And I click on float button
    And I click on "Add" Option
    When I enter issue title as <issue_title> and description as <issue_description> in boxes
    And I click on submit button
    Then I should see new issue title <issue_title> in issue list
    Examples:
      | Username   | Password         | repository_name | issue_title | issue_description      |
      | testofcafe | qacafebazaar2020 | cafebazaar/Hop  | Test        | issue_description test |






