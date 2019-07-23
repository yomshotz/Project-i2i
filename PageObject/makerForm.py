from Utility.actionKeys import MakeAction
from .Objects.uploadAndPhoto import UploadAndPhoto
from .Objects.sender import Sender
from .Objects.receiver import Receiver
from .Objects.maker import Maker
from .Objects.others import Others
import time

class MakerForm(object):

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

    def clickWallet(self):
        self.run.click_element(self.findBy, self.maker.tab_wallet)

    def clickNRPS(self):
        self.run.click_element(self.findBy, self.maker.tab_nrps)

    def clickSendMoney(self):
        self.run.click_element(self.findBy, self.maker.panel_sendMoney)

    def clickPanelWallet(self):
        self.run.click_element(self.findBy, self.maker.panel_wallet)

    def clickPanelInstapay(self):
        self.run.click_element(self.findBy, self.maker.panel_instapay)

    def clickPanelPesonet(self):
        self.run.click_element(self.findBy, self.maker.panel_pesonet)

    def detailsAndPhoto(self):
        self.run.click_element(self.findBy, self.maker.tab_details)

    def details(self):
        self.run.click_element(self.findBy, self.receiver.tab_details)

    def clickCancel(self):
        pass

