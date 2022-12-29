Feature: Ads
  Scenario: Waiting for an ad to be closed
    Given the ad
    When I will wait until it pops up
    Then I should be able to close it