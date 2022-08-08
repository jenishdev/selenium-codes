package resources;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Properties;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public class Base {
	
	    public WebDriver driver;
	    public Properties prop;
	
	public WebDriver initializedriver() throws IOException {
		 prop = new Properties();
		FileInputStream fis = new FileInputStream("C:\\Users\\JENISH\\eclipse-workspace\\EEframe\\src\\main\\java\\resources\\data.properties");
		
		prop.load(fis);
		
		String browserName = prop.getProperty("browser");
		System.out.println(browserName);
		
		if(browserName.equals("chrome")) {
			
			System.setProperty("webdriver.chrome.driver", "E://chromedriver.exe");
			 driver=new ChromeDriver();
			
		}
		else if(browserName.equals("firefox")) {
			System.setProperty("webdriver.gecko.driver", "E://geckodriver.exe");
			 driver = new FirefoxDriver();
			
		}
		
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		return driver;
		
		}

}
