import pytest
from PageObject.loginForm import Login
from PageObject.makerWallet import TransMakerWallet
from PageObject.makerPesonet import TransMakerPesonet
from PageObject.makerInstapay import TransMakerInstapay

@pytest.mark.usefixtures("setup")
class TestLoginForm:

    def test_transactionMaker(self):
        driver = self.driver
        run = Login(driver)
        transMakerWallet = TransMakerWallet(driver)
        transMakerPesonet = TransMakerPesonet(driver)
        transMakerInstapay = TransMakerInstapay(driver)

        username = "transmaker@testorg.com"
        password = "P@ssw0rd123!"

        run.login(username, password)
        transMakerWallet.makeWalletTransaction()
        #transMakerPesonet.makePesonetTransaction()
        #transMakerInstapay.makeInstapayTransaction()

