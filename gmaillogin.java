package Testcases;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

import objectrepository.loginpage;

public class gmaillogin {
	@Test
	
	
	public void login() {
		
		
		System.setProperty("webdriver.chrome.driver", "E:\\chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		
		driver.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin");
		loginpage ln = new loginpage(driver);
		ln.mailid().sendKeys("jenishdev007@gmail.com");
		ln.next1().click();
		ln.password1().sendKeys("dontbealooser");
		ln.nextp1().click();
		
		
		
		
	}
		
	}

	
	
