from Utility.actionKeys import MakeAction
from .Objects.receiver import Receiver
from .Objects.sender import Sender
from .Objects.others import Others
from .reuseGlobal import ReuseGlobal
from .makerForm import MakerForm
import time

class TransMakerInstapay(object):

    findBy = "xpath"

    def __init__(self, driver):
        self.driver = driver
        self.receiver = Receiver
        self.sender = Sender
        self.other = Others
        self.makerForm = MakerForm(driver)
        self.run = MakeAction(driver)
        self.reuse = ReuseGlobal(driver)

    def selectInstapayTransaction(self):
        self.run.capture_screen("Instapay Transaction")
        self.makerForm.clickNRPS()
        self.makerForm.clickSendMoney()
        time.sleep(2)
        self.makerForm.clickPanelInstapay()

    def setSenderInfo(self):
        self.run.find_element_and_input(self.findBy, self.sender.fld_accountSender, 1, "101400001643")
        self.run.find_element_and_input(self.findBy, self.sender.fld_lastname, 1, "Dela Cruz")
        self.run.find_element_and_input(self.findBy, self.sender.fld_firstname, 1, "Juan")
        self.run.find_element_and_input(self.findBy, self.sender.fld_middlename, 1, "Automated")
        self.run.find_element_and_input(self.findBy, self.sender.fld_address, 1, "#18 Sample Address,")
        self.run.find_element_and_input(self.findBy, self.sender.fld_mobile, 1, "9517284928")
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_gender)
        self.run.click_element(self.findBy, self.sender.fld_gender_specific)
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_area)
        self.run.click_element(self.findBy, self.sender.fld_area_specific)
        time.sleep(1)
        self.run.click_element(self.findBy, self.sender.fld_barangay)
        self.run.click_element(self.findBy, self.sender.fld_barangay_specific)
        time.sleep(1)
        self.reuse.clickNext(1)
        self.reuse.clickBack(1)
        self.reuse.clickNext(1)

    def setReceiverInfo(self):
        self.run.click_element(self.findBy, self.receiver.fld_bank)
        time.sleep(2)
        self.run.click_element(self.findBy, self.receiver.fld_bankInstapay_specific)
        time.sleep(10)

        self.run.find_element_and_input("xpath", "//input[@name='accountNumber']", 1, "101400001643")
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.receiver.fld_lastname, 1, "Dela Cruz")
        time.sleep(2)
        self.run.find_element_and_input(self.findBy, self.receiver.fld_firstname, 1, "Juan")
        self.run.find_element_and_input(self.findBy, self.receiver.fld_middlename, 1, "Automated")
        self.run.find_element_and_input(self.findBy, self.receiver.fld_address, 1, "#18 Sample Address,")
        time.sleep(1)
        self.run.find_element_and_input(self.findBy, self.receiver.fld_mobile, 1, "9517284928")
        time.sleep(1)
        self.run.click_element(self.findBy, self.receiver.fld_gender)
        self.run.click_element(self.findBy, self.receiver.fld_gender_specific)
        time.sleep(1)
        self.run.click_element(self.findBy, self.receiver.fld_area)
        self.run.click_element(self.findBy, self.receiver.fld_area_specific)
        time.sleep(1)
        self.run.click_element(self.findBy, self.receiver.fld_barangay)
        self.run.click_element(self.findBy, self.receiver.fld_barangay_specific)
        time.sleep(1)
        self.reuse.clickNext(1)
        time.sleep(5)

    def searchClient(self):
        self.reuse.clickSearchButton(1)

    def makeInstapayTransaction(self):
        self.selectInstapayTransaction()
        self.setSenderInfo()
        #self.setSenderInfo()
        self.setReceiverInfo()
