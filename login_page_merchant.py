import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


from Merchant.Testing.configuration.BasePage import BaseClass
from Merchant.Testing.configuration.testdata import TestData

class loginpage(BaseClass,TestData):


    mobile_number = (By.NAME, "username")
    password = (By.NAME, "password")
    button = (By.CSS_SELECTOR,"button[type='submit']")


    def login_merchant(self):
        self.enter_text(loginpage.mobile_number,TestData.username)
        self.enter_text(loginpage.password,TestData.password)
        self.do_click(loginpage.button)




