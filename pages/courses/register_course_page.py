from base.base_page import BasePage
import logging
import utilities.custom_logger as cl
import time


class RegisterCoursePage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


     ################
    ### Locators ###
    ################

    search_field = "search-courses"
    search_button = "//button[@id='search-course-button']"
    course_button = "//img[@class='course-box-image']"
    enroll_button = "enroll-button"
    card_number_field = "//div[@id='credit_card_number']"
    exp_date_field = "//div[@id='expiration']//div[@class='__PrivateStripeElement']//iframe[@frameborder='0']"
    post_code_field = "//div[@id='postal']//div[@class='__PrivateStripeElement']//iframe[@frameborder='0']"
    enroll_course_btn = "//button[@id='confirm-purchase']"
    enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"
    all_courses_link = "All Courses"


    ############################
    ### Element Interactions ###
    ############################


    def enter_search_field(self, course_name):
        self.send_keys(course_name, self.search_field)

    def click_search_button(self):
        self.element_click(self.search_button, locator_type="xpath")

    def select_course(self):
        self.element_click(self.course_button, locator_type="xpath")

    def click_enroll_button(self):
        self.element_click(self.enroll_button)

    def enter_card_num(self,num):
        self.send_keys(num, self.card_number_field, locator_type="xpath")

    def enter_exp_date(self,exp):
        self.send_keys(exp, self.exp_date_field,locator_type="xpath")

    def enter_post_code(self, cvv):
        self.send_keys(cvv, self.post_code_field, locator_type="xpath")

    def click_enroll_course_btn(self):
        self.element_click(self.enroll_course_btn, locator_type="xpath")

    def click_all_courses_link(self):
        self.element_click(self.all_courses_link, locator_type="link")

    def enter_credit_card_info(self, num, exp, cvv):
        self.enter_card_num(num)
        self.enter_exp_date(exp)
        self.enter_post_code(cvv)

    def enroll_course(self, num="", exp="", cvv=""):
        self.click_enroll_button()
        self.scroll_browser(direction="down")
        self.execute_script()
        self.enter_credit_card_info(num, exp, cvv)
        self.click_search_button()

    def verify_enroll_failed(self):
        message_element = self.wait_for_element(self.enroll_error_message, locator_type="xpath")
        result = self.is_element_displayed(element=message_element)
        return result























