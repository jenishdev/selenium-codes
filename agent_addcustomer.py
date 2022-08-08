from selenium.webdriver.common.by import By

from Merchant.Testing.merchant.configuration.BasePage import BaseClass
from agent.Configuration_agent.testdata_agent import testdata_agent


class add_customer(BaseClass):
    click_add_customer = (By.XPATH,"//div[@class='sidenav']/a[8]")
    click_add_customer_btn = (By.LINK_TEXT,"customer_add")
    first_name = (By.XPATH,"//input[@name='first_name']")
    last_name = (By.XPATH, "//input[@name='last_name']")
    phone_no = (By.XPATH, "//input[@name='phone_no']")
    Email = (By.XPATH, "//input[@name='email']")
    id_proof = (By.XPATH, "//select[@name='type_of_id']")
    id_proof_no = (By.XPATH, "//input[@name='id_number']")
    attach_file = (By.XPATH, "//input[@name='first_name']")
    submit = (By.XPATH, "//button[@type='submit']")

def add_customer_method(self):
    self.do_click(add_customer.click_add_customer)
    self.do_click(add_customer.click_add_customer_btn)
    self.enter_text(add_customer.first_name,testdata_agent.fname_add_cus)
    self.enter_text(add_customer.last_name,testdata_agent.lname_add_cus)
    self.enter_text(add_customer.phone_no,testdata_agent.phno_add_cus)
    self.enter_text(add_customer.Email,testdata_agent.email_add_cus)
    self.drop_down(add_customer.id_proof,"addhar")
    self.enter_text(add_customer.id_proof_no,testdata_agent.id_no_add_cus)
    self.attach_file(add_customer.attach_file)
    self.do_click(add_customer.submit)

