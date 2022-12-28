Feature: Click Events
  Scenario Outline:
    Given buttons of the animals
    When I click "<button>"
    Then the "<sound>" of that animal should appear on the screen

    Examples:
    |button|sound|
    |Cat   |Meow!|
    |Pig   |Oink!|
    |Dog   |Woof!|
    |Cow   |Moo! |
