Feature: Front Page

    Scenario: User_can_open_Women_Store
        Given I am opening page "/index.php"
        When I am clicking on "a[title="Women"]"
        Then I am verifying title with "Women - My Store"
        #Given Open Page "/index.php?controller=contact"

    Scenario: User_can_open_CONTACT_US_page
      Given I am opening page "/index.php"
      When I am clicking on "a[title="Contact Us"]"
      Then I am verifying title with "Contact us - My Store"
