import pytest
from selenium import webdriver

from Merchant.Testing.merchant.configuration.BaseClass import Baseclas
from Merchant.Testing.configuration.BasePage import BaseClass
from Merchant.Testing.configuration.conftest import setup
from Merchant.Testing.configuration.testdata import TestData
from Merchant.Testing.merchant.pages.Received_payments import received_payments
from Merchant.Testing.pages.login_page_merchant import loginpage
from Merchant.Testing.merchant.pages.transfer_money import transfer_money1


class Testlogin(Baseclas):

    #def test_login(self):
        #login1 = loginpage(self.driver)
        #login1.login_merchant()
    def test_received_payments(self):
        view_payments = received_payments(self.driver)
        view_payments.received_payment_page()
    #def test_refund_view(self):
        #refund_view = received_payments(self.driver)
        #refund_view.refund_payment()

    #class Testtransfermoney(Baseclas):
    def test_transfermoney(self):
        transfer_mon = transfer_money1(self.driver)
        transfer_mon.transfer_money_page()

