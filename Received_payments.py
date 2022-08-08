import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

from Merchant.Testing.configuration import testdata
from Merchant.Testing.configuration.BasePage import BaseClass
from Merchant.Testing.configuration.testdata import TestData


class received_payments(BaseClass):
    received_payments1 = (By.XPATH, "//div[@class='sidenav']/a[2]")
    refund = (By.XPATH, "//table[@id='myTable']/tbody/tr[5]/td[7]/button")
    refund1 =(By.NAME, "refund_payment")
    refund2 =(By.XPATH, "//input[@id='password']")


    def received_payment_page(self):
        self.do_click(received_payments.received_payments1)

    def refund_payment(self):
       self.do_click(received_payments.refund)
       self.is_alert_present(self.driver)
       self.enter_text(received_payments.refund1, TestData.refund_amount)

       self.enter_text(received_payments.refund2, TestData.transaction_pin)

       #print(alert.text())




