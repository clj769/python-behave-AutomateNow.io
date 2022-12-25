Feature: Tables

  Scenario: Simple table (item prices)
    Given the simple table
    When I extract data from the table
    Then the values will be available for analysis

  Scenario: Sortable table - search box
    Given the search input field
    When I type rank, country or population
    Then the table should show only the row of interest

  Scenario: Sortable table - show 10 or 25 results
    Given the "show" dropdown list
    When I choose 10 or 25 from that dropdown menu
    Then the table should show only 10 or 25 results

  Scenario: Sortable table - sorting columns
    Given the sorting of column option by clicking its name
    When I click the name of the column
    Then the table should be sorted ascending/descending

  Scenario: Sortable table - previous/next buttons
    Given the previous/next buttons
    When I click previous/next button
    Then the table should show only the row of interest
    And text below table should show how many of how many entries are shown
