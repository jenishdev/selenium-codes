package pageobject;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class loginpage {
	
	public WebDriver driver;
	
	public loginpage(WebDriver driver) {
		
		this.driver = driver;   // assigns the driver from the testcase to the driver created here
	}
	
	By mobilenumber = By.cssSelector("input[name='username']");
	By password = By.cssSelector("input[name='password']");
	By submit = By.cssSelector("button[type='submit']");
	By invalidtext = By.cssSelector(".log-txt>p");
	
	
	public WebElement getmobilenumber() {
		
		return driver.findElement(mobilenumber);
		
		
	}
	
	public WebElement getpassword() {
		
		return driver.findElement(password);
	}
	
	public WebElement getsubmit() {
		
		return driver.findElement(submit);
	}
	
	public WebElement errormessage() {
		return driver.findElement(invalidtext);
	}

}
