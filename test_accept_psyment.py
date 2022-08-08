from Merchant.Testing.merchant.configuration.BaseClass import Baseclas
from Merchant.Testing.merchant.configuration.BasePage import BaseClass
from Merchant.Testing.merchant.configuration.conftest import setup
from Merchant.Testing.merchant.pages.accept_payment import accept_payment


class Testacceptpayment(Baseclas):
    def test_acceptpayment(self):
        super().__init__()
        accept = accept_payment(self.driver)
        accept.accept_payment1()
