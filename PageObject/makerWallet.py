from Utility.actionKeys import MakeAction
from .Objects.sender import Sender
from .Objects.receiver import Receiver
from .Objects.maker import Maker
from .Objects.amountAndPurpose import AmountAndPurpose
from .Objects.uploadAndPhoto import UploadAndPhoto
from .makerForm import MakerForm
from .reuseGlobal import ReuseGlobal
from .Objects.others import Others

import time
import datetime

class TransMakerWallet(object):

    now = datetime.datetime.now()
    year = str(now.year)
    date = str(now.day)

    findBy = "xpath"
    findByTag = "tag_name"
    tag_for_scroll = "body"

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)
        self.photo = UploadAndPhoto(driver)
        self.reuse = ReuseGlobal(driver)

        self.sender = Sender
        self.receiver = Receiver
        self.maker = Maker
        self.amount = AmountAndPurpose
        self.other = Others

        self.makerForm = MakerForm(driver)

    def setSenderInfo(self):
        self.run.find_element_and_input(self.findBy, self.sender.fld_lastname, 1, "Dela Cruz")
        self.run.find_element_and_input(self.findBy, self.sender.fld_firstname, 1, "Juan")
        self.run.find_element_and_input(self.findBy, self.sender.fld_middlename, 1, "Automated")
        self.run.find_element_and_input(self.findBy, self.sender.fld_address, 1, "#18 Sample Address,")
        self.run.click_element(self.findBy, self.sender.fld_area)
        self.run.click_element(self.findBy, self.sender.fld_area_specific)
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_barangay)
        self.run.click_element(self.findBy, self.sender.fld_barangay_specific)
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_nationality)
        self.run.click_element(self.findBy, self.sender.fld_nationality_specific)
        time.sleep(1)
        self.run.find_element_and_input(self.findBy, self.sender.fld_mobile, 1, "9517284928")
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_gender)
        self.run.click_element(self.findBy, self.sender.fld_gender_specific)
        time.sleep(1)
        self.reuse.setBirthdate()
        self.run.find_element_and_input(self.findBy, self.sender.fld_birthPlace, 1, "Sample City")
        time.sleep(1)
        self.reuse.setScrollDown()
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_ID)
        self.run.click_element(self.findBy, self.sender.fld_ID_specific)
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.sender.fld_ID_number, 1, "123123")
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_funds)
        self.run.click_element(self.findBy, self.sender.fld_funds_specific)
        time.sleep(1)
        self.run.find_element_and_input(self.findBy, self.sender.fld_email, 1, "jigsgulapa@gmail.com")
        time.sleep(1)
        self.run.capture_screen("Sender Details")

    def setReceiverInfo(self):
        self.run.find_element_and_input(self.findBy, self.receiver.fld_lastname, 1, "Yom")
        self.run.find_element_and_input(self.findBy, self.receiver.fld_firstname, 1, "Yom")
        self.run.find_element_and_input(self.findBy, self.receiver.fld_middlename, 1, "Yom")
        self.run.find_element_and_input(self.findBy, self.sender.fld_mobile, 1, "9517284928")

    def setAmountAndPurpose(self):
        self.run.find_element_and_input(self.findBy, self.amount.fld_amount, 1, "1000")
        self.run.find_element_and_input(self.findBy, self.amount.fld_beneficiary, 1, "Brader")
        time.sleep(1)
        self.run.click_element(self.findBy, self.amount.fld_purpose)
        self.run.click_element(self.findBy, self.amount.fld_purpose_specific)
        time.sleep(1)
        self.reuse.setScrollDown()

    def confirmationPage(self):
        time.sleep(1)
        self.reuse.setScrollUp()
        self.run.capture_screen("Confirmation Page - Top")
        time.sleep(1)
        self.reuse.setScrollDown()
        self.run.capture_screen("Confirmation Page - Bottom")

    def selectWalletTransaction(self):
        self.run.capture_screen("Wallet Transaction")
        self.makerForm.clickWallet()
        self.makerForm.clickSendMoney()
        self.makerForm.clickPanelWallet()
        self.makerForm.detailsAndPhoto()
        time.sleep(4)

    def settingUpSender(self):
        self.setSenderInfo()
        self.reuse.clickNext(2)
        self.photo.takePhoto(2)
        self.reuse.clickNext(2)

    def settingUpReceiver(self):
        time.sleep(2)
        self.reuse.setScrollUp()
        time.sleep(1)
        self.makerForm.details()
        self.setReceiverInfo()
        self.reuse.clickNext(1)
        self.setAmountAndPurpose()
        self.reuse.clickNext(1)

    def checkConfirmationPage(self):
        self.confirmationPage()
        self.reuse.clickNext(1)
        self.reuse.clickOk()
        time.sleep(8)

    def checkReceiptPage(self):
        self.run.capture_screen("Receipt Page")
        time.sleep(1)
        self.run.click_element(self.findBy, self.other.btn_done)
        time.sleep(3)

    def makeWalletTransaction(self):
        self.selectWalletTransaction()
        self.settingUpSender()
        self.settingUpReceiver()
        self.checkConfirmationPage()
        self.checkReceiptPage()
