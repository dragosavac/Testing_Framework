from base.base_page import BasePage
import logging
import utilities.custom_logger as cl
import random
import time


class RegisterPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    register_link = "//button[@id='test-reg-button']"
    name_field = "//input[@id='fos_user_registration_form_name']"
    email_field = "fos_user_registration_form_email"
    password_field = "fos_user_registration_form_plainPassword"
    sign_up_button = "//button[@class='btn btn-red padding--hor2x js-signin-button']"
    welcome_message = "//h2[@class='cl-white text--normal text--28'][contains(text(),'Welcome to Kindergifts')]"
    name_error_message = "//span[@class='error'][contains(text(),'Please enter a name.')]"
    email_error_message = "//span[@class='error'][contains(text(),'Please enter an email address')]"
    password_error_message = "//span[@class='error'][contains(text(),'Please enter a password.')]"
    invalid_email_error_message = "//span[@class='error'][contains(text(),'Please enter a valid email address.')]"
    invalid_password_error_message = "//span[@class='error'][contains(text(),'Please enter a valid email address.')]"
    already_reg_user_error = "//span[@class='error'][contains(text(),'This email is already used, please try another one.')]"
    rand_int = random.randint(15, 298777)
    random_user = "rade.dragosavac+" + str(rand_int) + "@etondigital.com"

    def click_register_link(self):
        self.element_click(self.register_link, locator_type="xpath")

    def enter_name_field(self, name):
        self.send_keys(name, self.name_field, locator_type="xpath")

    def enter_email_field(self, email):
        self.send_keys(email, self.email_field)

    def enter_password_field(self, password):
        self.send_keys(password, self.password_field)

    def click_sign_up_button(self):
        self.element_click(self.sign_up_button, locator_type="xpath")

    def register(self, name="", email="", password=""):
        self.click_register_link()
        self.enter_name_field(name)
        self.enter_email_field(email)
        self.enter_password_field(password)
        self.click_sign_up_button()

    def verify_registration_passed(self):
        result = self.is_element_present(self.welcome_message, locator_type="xpath")
        return result

    def verify_empty_error_messages(self):
        self.is_element_present(self.name_error_message, locator_type="xpath")
        self.is_element_present(self.email_error_message, locator_type="xpath")
        self.is_element_present(self.password_error_message, locator_type="xpath")

    def verify_invalid_error_messages(self):
        self.is_element_present(self.invalid_email_error_message, locator_type="xpath")
        self.is_element_present(self.invalid_password_error_message, locator_type="xpath")

    def verify_already_reg_user(self):
        self.is_element_present(self.already_reg_user_error, locator_type="xpath")
