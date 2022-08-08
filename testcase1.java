import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class testcase1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	System.setProperty("webdriver.chrome.driver", "F:\\chromedriver.exe");
		
		WebDriver driver=new ChromeDriver();
		driver.get("http://facebook.com");
		driver.findElement(By.id("email")).sendKeys("jenishonline2006@yahoo.co.in");//click inspect and fine id
		driver.findElement(By.name("pass")).sendKeys("abcd");// similar to above step
		driver.findElement(By.linkText("Forgotten password?")).click();// since it is redirect to another page link text and to do click action
		driver.findElement(By.cssSelector("div#error.loginError")).getText();
	}

}