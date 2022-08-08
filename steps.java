package stepdefinition;

import org.junit.runner.RunWith;

import cucumber.api.java.en.And;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
public class steps {

	 @Given("^User is on the net banking landing page$")
	 public void user_is_on_the_net_banking_landing_page() {
		 System.out.println("landing page");
	    }

	 @When("^user login to the application with \"([^\"]*)\" and \"([^\"]*)\"$")
	 public void user_login_to_the_application_with_something_and_something(String strArg1, String strArg2)throws Throwable {

	    
	         System.out.println(strArg1);
	         System.out.println(strArg2);
	 	    
	    
	    }

	  @Then("^Home page is populated$")
	  public void home_page_is_populated(){
	    
	    System.out.println("landing page");
	    }

	   @And("^cards are dislayed$")
	   public void cards_are_dislayed() {
	    
	    	System.out.println("landing page");
	    }

}
