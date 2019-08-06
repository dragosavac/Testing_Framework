from base.base_page import BasePage
import utilities.custom_logger as cl
import logging
import time


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_link = "//li[@class='d--ib']//button[@class='btn-reset text--15 text--normal text--upper js-pre-login-modal-button']"
    email_field = "username"
    password_field = "password"
    login_button = "//button[@id='_submit']"
    error_message = "//p[contains(text(),'Your email or password are incorrect. Please try again.')]"
    user_icon = "//div[@class='pull-right']//button[@type='button']"

    def click_login_link(self):
        self.element_click(self.login_link, locator_type="xpath")

    def enter_email(self, email):
        self.send_keys(email, self.email_field)

    def enter_password(self, password):
        self.send_keys(password, self.password_field)

    def click_login_button(self):
        self.element_click(self.login_button, locator_type="xpath")

    def login(self, email="", password=""):
        time.sleep(3)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result = self.is_element_present(self.user_icon, locator_type="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(self.error_message, locator_type="xpath")
        return result

    def verify_login_title(self):
        return self.verify_page_title("Kindergifts")










