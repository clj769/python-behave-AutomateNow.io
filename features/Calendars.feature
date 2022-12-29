Feature: Calendars
  Scenario: Selecting date
    Given the calendar
    When I select the date
    Then I should be able to see selected date on the next page
