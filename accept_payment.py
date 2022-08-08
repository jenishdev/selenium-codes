from selenium.webdriver.common.by import By

from Merchant.Testing.configuration.BasePage import BaseClass
from Merchant.Testing.configuration.testdata import TestData


class accept_payment(BaseClass,TestData):

    page_accept = (By.XPATH, "//div[@class='sidenav']/a[6]")
    mobile_number_ap = (By.ID, "wallet_check")
    amount_ap = (By.ID, "amount")
    pin_ap = (By.NAME, "transaction_pin")
    submit_ap = (By.ID, "submit_s")


    def accept_payment1(self):
        self.do_click(accept_payment.page_accept)
        self.enter_text(accept_payment.mobile_number_ap,TestData.mob_transfer_money)
        self.enter_text(accept_payment.amount_ap,TestData.amount_transfer_money)
        self.enter_text(accept_payment.pin_ap,TestData.transac_pin_transf_money)
        self.do_click(accept_payment.submit_ap)

