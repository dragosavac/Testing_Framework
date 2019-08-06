from base.base_page import BasePage
import logging
import utilities.custom_logger as cl


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    login_link = "Login"
    email_field = "user_email"
    password_field = "user_password"
    login_button = "//input[@type='submit']"
    user_icon = "//span[@class='navbar-current-user']"
    error_message = "// div[contains(text(),'Invalid email or password')]"

    def click_login_link(self):
        self.element_click(self.login_link, locator_type="link")

    def enter_email(self, email):
        self.send_keys(email, self.email_field)

    def enter_password(self, password):
        self.send_keys(password, self.password_field)

    def click_login_button(self):
        self.element_click(self.login_button, locator_type="xpath")

    def login(self, email="", password=""):
        self.click_login_link()
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
        return self.verify_page_title("Let's Kode It")







# This was previous solution

 # def get_login_link(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self.email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self.password_field)
    #
    # def get_login_button(self):
    #     return self.driver.find_element(By.XPATH, self.login_button)
