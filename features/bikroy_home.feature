Feature: Bikroy.com home page

  Scenario: all category name presence
    Given launch chrome browser
    When open bikroy.com home page
    Then veryfy that all category name are visible
    And close the browser
