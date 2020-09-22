# Created by ali at 9/20/20
Feature: Edit exist issue on Cafebazaar Hop project

  @device-AndroidEmulator
  Scenario Outline: Login in to account with correct user info (Basic Authentication method) search Cafebazaar Hop project and
  edit the issue
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
    And I click on issue title <recent_issue_title>
    And I click edit icon
    When I update <issue_title> and <issue_description> in boxes
    And I click on submit button
    Then I should see new issue title <issue_title> in issue list
    Examples:
      | Username   | Password         | repository_name | recent_issue_title | issue_title      | issue_description           |
      | testofcafe | qacafebazaar2020 | cafebazaar/Hop  | Test               | edit_issue_title | edit_issue_description test |