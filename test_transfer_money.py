import pytest

from Merchant.Testing.configuration.BaseClass import Baseclas
from Merchant.Testing.configuration.conftest import setup
from Merchant.Testing.pages.transfer_money import transfer_money1

class Testtransfermoney(Baseclas):
    def test_transfermoney(self):
        super().__init__()
        transfer_mon = transfer_money1(self.driver)
        transfer_mon.transfer_money_page()