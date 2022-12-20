Feature: JavaScript Delays
  Scenario: Countdown timer works as expected
    Given countdown timer with a start button
    And picture of a rocket ship
    When START button is clicked
    Then after 10 seconds "Liftoff!" appears in the text field