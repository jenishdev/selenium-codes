import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from Merchant.Testing.configuration.testdata import TestData
from agent.Configuration_agent.testdata_agent import testdata_agent


@pytest.fixture(scope="class")
def setup_agent1(request):
    # Setting up how we want Chrome to run
    driver = webdriver.Chrome(testdata_agent.executable_path)
    # browser should be loaded in maximized window
    driver.get(testdata_agent.Base_Url)
    driver.maximize_window()
    driver.find_element_by_name('username').send_keys("84654884")
    driver.find_element_by_name('password').send_keys("1234")
    driver.find_element_by_css_selector("button[type='submit']").click()
    #driver.get(TestData.Base_Url)
    request.cls.driver = driver
    yield
    driver.close()
