Feature: Application login

Scenario: Home page default login
 Given User is on the net banking landing page
 When user login to the application with "jenish" and "dev"
 Then Home page is populated
 And cards displayed are "true"
 
 Scenario: Home page default login
 Given User is on the net banking landing page
 When user login to the application with "jenish" and "dev1"
 Then Home page is populated
 And cards displayed are "false"