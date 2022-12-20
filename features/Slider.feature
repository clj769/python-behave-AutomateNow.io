Feature: Slider

  Scenario: Slider works as expected by adjusting it by using drag-and-drop operation
    Given the slider
    When I adjust it by using drag-and-drop operation
    Then the current value will be updated

  Scenario: Slider works as expected by clicking a given area of the slider
    Given the slider once again
    When I adjust it by clicking a given area of the slider
    Then the current value will be updated once again
