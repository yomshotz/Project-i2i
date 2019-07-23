from Utility.actionKeys import MakeAction
import time

class UploadAndPhoto(object):

    findBy = "xpath"
    fld_upload = "//*[@id='root']/div/div/div/div[4]/div[2]/div/div[2]" \
                 "/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]"

    btn_take_photo = "//span[contains(text(), 'Take Photo')]"
    btn_capture = "//span[contains(text(), 'Capture')]"

    photoSample = "D:\\sample.jpg"

    def __init__(self, driver):
        self.driver = driver
        self.run = MakeAction(driver)

    def uploadPhoto(self, ntime: int):
        time.sleep(ntime)
        self.run.find_element_and_input(self.findBy, self.fld_upload, 1, self.photoSample)
        time.sleep(ntime)

    def takePhoto(self, ntime: int):
        time.sleep(ntime)
        self.run.click_element(self.findBy, self.btn_take_photo)
        time.sleep(ntime)
        self.run.click_element(self.findBy, self.btn_capture)


