import pytest
from PageObject.loginForm import Login

@pytest.mark.usefixtures("setup")
class TestLoginForm:

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_login(self):
        driver = self.driver
        run = Login(driver)

        username = "ccylim@unionbankph.com"
        password = "P@ssw0rd123!"

        run.login(username, password)
