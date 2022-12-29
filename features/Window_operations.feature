Feature: Window operations
  Scenario Outline: Managing windows in the browser
    Given window operations
    When I choose <operation>
    Then I should manage <operation> accordingly

    Examples:
    |operation|
    |new_tab   |
    |replace_window|
    |new_window    |