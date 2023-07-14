Feature: Broken Images
  Scenario: Detection of broken images
    Given the images
    When the site is loaded
    Then the images should be properly displayed
