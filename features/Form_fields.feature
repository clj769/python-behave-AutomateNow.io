Feature: Form fields
  Scenario: Filling out  the form
    Given the form
    When I fill the form and click submit
    Then I should see message sent confirmation