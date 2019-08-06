from base.base_page import BasePage
import logging
import utilities.custom_logger as cl


class NavigationPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    my_courses = "My Courses"
    all_courses = "All Courses"
    practice = "Practice"
    user_settings_icon = "//span[@class='navbar-current-user']"

    def navigate_to_all_courses(self):
        self.element_click(self.all_courses, locator_type="link")

    def navigate_to_my_courses(self):
        self.element_click(self.my_courses, locator_type="link")

    def navigate_to_practice(self):
        self.element_click(self.practice, locator_type="link")

    def navigate_to_user_icon(self):
        self.element_click(self.user_settings_icon, locator_type="xpath")

