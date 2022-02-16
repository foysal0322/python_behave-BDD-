Feature: Bikroy.com login

  Scenario Outline: login bikroy.com with valid credentials

    Given launch browser
    When open bikroy.com login page
    And click "continue with email"
    And enter "<email>" and "<password>"
    And click login button
    Then User must successfully jump to the dashboard

    Examples:
      | email                | password      |
      | abcd@gmail.com       | testpass1234  |
      | fasleemail@gmail.com | wrongpassword |
      | foysal0322@gmail.com | foysal03      |



