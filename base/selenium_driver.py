from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import time
import os
import utilities.custom_logger as cl


class SeleniumDriver():

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, result_message):

        file_name = result_message + "." + str(round(time.time()*1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot save to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type +
                          " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator +
                          " and locatorType: " + locator_type)
        except:
            self.log.error("Element not found with locator: " + locator +
                           " and locatorType " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            byType = self.get_by_type(locator_type)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.error("Can't click on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def send_keys(self, data, locator="", locator_type = "id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
                element.clear()
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            self.log.error("Can't send data on the element with locator: " + locator +
                          " locatorType: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type = "id", element=None, info=""):

        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locator_type = "id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locator_type)
                return True
            else:
                self.log.error("Element not present with locator: " + locator +
                              " locatorType: " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def is_element_missing(self, locator="", locator_type = "id", element=None):
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is None:
                self.log.info("Element with locator: " + locator +
                              " locatorType: " + locator_type + " is missing")
                return True
            else:
                self.log.error("Element with locator: " + locator +
                              " locatorType: " + locator_type + " is not missing")
                return False
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, byType):
        try:
            element_list = self.driver.find_elements(byType, locator)
            if len(element_list) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.error("Element not found")
                return False
        except:
            self.log.error("Element not found")
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):

        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            else:
                self.log.error("Element not displayed with locator: " + locator +
                              " locatorType: " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    def wait_for_element(self, locator, locator_type = "id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def scroll_browser(self, direction="up"):

        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def execute_script(self):
        self.driver.execute_script("window.scrollBy(0, -150);")

    def scroll_into_view(self, element, locator_type):
            self.get_element(element, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)




















