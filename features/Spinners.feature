Feature: Broken Images
  Scenario: Spinner is displayed on page load
    Given the spinner element
    When I wait for the spinner to be present on the page
    Then the spinner should be displayed on the page
