from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from Utility import helper
from datetime import datetime

class MakeAction(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_visible(self, by, locator, wait=3):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.visibility_of_element_located((by, locator))
            )
            if element:
                print("Element {0} Found".format(locator))
                return True
            else:
                print("Element {0} Not Found".format(locator))
                return False
        except TimeoutException:
            print("Element {0} Not Found".format(locator))
            return False

    def wait_until_element_not_visible(self, by, locator, wait=5):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.invisibility_of_element_located((by, locator))
            )
            if element:
                return True
        except TimeoutException as e:
            print(e)
            return False

    def click_element(self, by, locator, wait=7):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.element_to_be_clickable((by, locator))
            )
            element.click()
            print('Click Element || Element Found {0}'.format(locator))
            return True
        except (NoSuchElementException, WebDriverException, TimeoutException) as e:
            print('Unable to click the element {0} '.format(locator)+str(e))
            message = "Unable to find element"
            self.capture_screen(message)
            return False

    def find_elements(self, by: str, locator: str, wait=7):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, int(wait)).until(
                EC.visibility_of_element_located((by, locator))
            )
            print("Element " + locator + " Found")
            return element
        except TimeoutException:
            message = "Unable to find element"
            print("Find_Elements {0} has reached Timeout Exception".format(locator))
            self.capture_screen(message)
            return None

    def find_element_by_tagname(self, by: str, locator: str, wait=7):
        by = helper.method_by(by)
        try:
            element = WebDriverWait(self.driver, int(wait)).until(
                EC.visibility_of_element_located((by, locator))
            )
            print("Element " + locator + " Found")
            return element
        except TimeoutException:
            message = "Unable to locate tag element"
            print("Find_Elements {0} has reached Timeout Exception".format(locator))
            self.capture_screen(message)
            return None

    def find_element_and_input(self, by: str, locator: str, wait: int, text: str):
        element = self.find_elements(by, locator, wait)
        if element:
            element.send_keys(text)
            return True
        else:
            return False

    def find_item_in_elements_and_click(self, by:str, locator: str, wait: int, selectItem: str):
        by = helper.method_by(by)

        try:
            element = WebDriverWait(self.driver, int(wait)).until(
                EC.visibility_of_all_elements_located((by, locator))
            )
            for i in element:
                if i.text == selectItem:
                    i.click()
                    print("{} is selected".format(selectItem))
                    return True
                else:
                    print("Not found")

        except (NoSuchElementException, WebDriverException, TimeoutException):
            message = "Unable to locate elements"
            print("Find_Elements {0} has reached Timeout Exception".format(locator))
            self.capture_screen(message)

    def web_scroll(self, direction, by, locator):
        try:
            if direction == 'up':
                tagname = self.find_element_by_tagname(by, locator)
                tagname.send_keys(Keys.CONTROL + Keys.HOME)
                print("Scroll up")
                return True
            elif direction == 'down':
                tagname = self.find_element_by_tagname(by, locator)
                tagname.send_keys(Keys.CONTROL + Keys.END)
                print("Scroll down")
                return True
            elif direction == 'right':
                self.driver.execute_script("window.scrollTo(1000,0)")
                print("Scroll right")
                return True
            elif direction == 'left':
                self.driver.execute_script("window.scrollTo(-1000,0)")
                print("Scroll left")
                return True
            else:
                print("Unable to scroll - Invalid keyword")
                return False
        except:
            message = "Unable to scroll"
            print("Unable to scroll")
            self.capture_screen(message)
            return False

    def capture_screen(self, filename):
        now = datetime.now()
        try:
            folder_location = "C:\\Users\\cheqws115-user\\PycharmProjects\\Project_Siargao\\Screenshots\\"
            my_time = now.strftime("%m-%d-%Y %H-%M-%S")
            destination = folder_location + my_time + " " + filename + ".png"
            self.driver.save_screenshot(destination)
            print("Screen capture")
            return True
        except NotADirectoryError:
            print("Unable to capture screen")
            return False

    def get_title(self):
        return self.driver.title







