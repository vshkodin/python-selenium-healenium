Feature: Front Page


    Scenario: User_can_open_Women_page
        Given I am opening page "/index.php"
        When I am clicking on "a[title="Women"]"
        Then I am verifying title with "Women - My Store"


    Scenario: User_can_open_Contact_Us_page
      Given I am opening page "/index.php"
      When I am clicking on "a[title="Contact Us"]"
      Then I am verifying title with "Contact us - My Store"