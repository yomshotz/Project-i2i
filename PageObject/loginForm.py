from Utility.actionKeys import MakeAction
from .otpForm import Otp
import time

class Login(object):

    findBy = 'xpath'
    findByTag = 'tag_name'
    fld_username = "//input[@name='email']"
    fld_password = "//input[@name='password']"
    fld_btnLogin = "//span[contains(text(), 'Log In')]"
    tag_for_scroll = 'body'

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)
        self.otp = Otp(driver)

    def setUsername(self, username):
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.fld_username, 1, username)

    def setPassword(self, password):
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.fld_password, 1, password)

    def clickLogin(self):
        time.sleep(2)
        self.run.click_element(self.findBy, self.fld_btnLogin, 1)

    def setScrollDown(self):
        self.run.web_scroll("down", self.findByTag, self.tag_for_scroll)

    def setScrollUp(self):
        self.run.web_scroll("up", self.findByTag, self.tag_for_scroll)

    def login(self, username, password):
        # self.setScrollDown()
        # time.sleep(5)
        self.setUsername(username)
        self.setPassword(password)
        self.clickLogin()
        self.otp.run_otp()
        # time.sleep(5)
