import pytest
from selenium.webdriver.common.by import By

from Merchant.Testing.configuration.BasePage import BaseClass
from Merchant.Testing.configuration.testdata import TestData


class transfer_money1(BaseClass):
    transfer = (By.XPATH, "//div[@class='sidenav']/a[4]")
    transfer_to = (By.ID, "wallet_type")
    wallet_no = (By.NAME, "wallet_id")
    amount = (By.NAME, "amount")
    transaction_pin = (By.NAME, "trans_pin")
    reference = (By.NAME, "reference")
    submit = (By.CSS_SELECTOR, "//button[id='submit_s']")

    def transfer_money_page(self):
        self.do_click(transfer_money1.transfer)
        self.drop_down(transfer_money1.transfer_to, "Customer")
        self.enter_text(transfer_money1.wallet_no, TestData.mob_transfer_money)
        self.enter_text(transfer_money1.amount, TestData.amount_transfer_money)
        self.enter_text(transfer_money1.transaction_pin,TestData.transac_pin_transf_money)
        self.enter_text(transfer_money1.reference, TestData.Reference)
        self.do_click(transfer_money1.submit)

