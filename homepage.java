package Ecomframe.EEframe;

import java.io.IOException;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import pageobject.loginpage;
import resources.Base;

public class homepage extends Base {
	
	public static Logger log = LogManager.getLogger(homepage.class.getName());
	
	
	@BeforeTest
	
	  public void hiturl() throws IOException {
		
		driver = initializedriver();
		log.info("driver is initialized");
		driver.get(prop.getProperty("url"));
		log.info("login page is reached");
	}
	
       // @Test(dataProvider = "getdata")
	
	@Test
        
        //public void basepagenavigation(String username,String password) throws IOException {
	
	public void basenavigation() {
        	
        	
		
		
		loginpage lp = new loginpage(driver);
		lp.getmobilenumber().sendKeys(prop.getProperty("username"));
		lp.getpassword().sendKeys(prop.getProperty("password"));
		lp.getsubmit().click();
		
		
	}
        
//        @DataProvider
//        
//        public Object[][] getdata() {
//        	
//        	Object[][] data = new Object[2][2];
//        	
//        	data[0][0] = "89284585";
//        	data[0][1] = "alizza@admin";
//        	data[1][0] = " alizza@admin";
//        	data[1][1] = "alizza@admin";
//        	
//        	return data;
//        }
        
        @AfterTest
        public void closedriver() {
        	driver.close();
        }
        
}


