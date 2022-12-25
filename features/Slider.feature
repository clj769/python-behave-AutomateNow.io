Feature: Slider

  Scenario Outline: Slider works as expected by adjusting it by using drag-and-drop operation
    Given the slider
    When I adjust it by <using> drag-and-drop or clicking a given-area operation
    Then the current value will be updated

Examples:
  | using |
  |drag_and_drop|
  |given_area|
