from Utility.actionKeys import MakeAction
from .Objects.uploadAndPhoto import UploadAndPhoto
from .Objects.sender import Sender
from .Objects.receiver import Receiver
from .Objects.maker import Maker
from .Objects.others import Others
from selenium.webdriver.common.keys import Keys
import time

class ReuseGlobal(object):

    findBy = "xpath"
    findByTag = "tag_name"
    tag_for_scroll = "body"

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)
        self.photo = UploadAndPhoto(driver)
        self.sender = Sender
        self.receiver = Receiver
        self.maker = Maker
        self.other = Others

    def setScrollDown(self):
        self.run.web_scroll("down", self.findByTag, self.tag_for_scroll)

    def setScrollUp(self):
        self.run.web_scroll("up", self.findByTag, self.tag_for_scroll)

    def setBirthdate(self):
        self.run.click_element(self.findBy, self.sender.fld_birthday)
        self.run.click_element(self.findBy, self.sender.fld_year)
        self.run.click_element(self.findBy, self.sender.fld_year_specific)
        self.run.click_element(self.findBy, self.sender.fld_date)

    def clickOk(self):
        self.run.click_element(self.findBy, self.other.btn_ok)

    def clickDone(self):
        self.run.click_element(self.findBy, self.other.btn_done)

    def clickNext(self, ntime: int):
        time.sleep(ntime)
        self.run.click_element(self.findBy, self.other.btn_next)
        time.sleep(ntime)

    def clickBack(self, ntime: int):
        time.sleep(ntime)
        self.run.click_element(self.findBy, self.other.btn_back)
        time.sleep(ntime)

    def clickSearchButton(self, ntime: int):
        self.run.click_element(self.findBy, self.other.btn_search)
        self.searchClient(ntime)
        time.sleep(ntime)

    def searchClient(self, ntime: int):
        self.run.find_element_and_input(self.findBy, self.other.fld_search, 1, "t")
        self.run.find_element_and_input(self.findBy, self.other.fld_search, 1, Keys.ENTER)
        time.sleep(ntime)
