Feature: Gestures
  Scenario Outline: Managing windows in the browser
    Given gestures examples
    When I choose <element> element
    Then I should manage <element> element accordingly

    Examples:
    |element|
    |move_me_around|
    |drag_and_drop |
    |drag_the_map  |