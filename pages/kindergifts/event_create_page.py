from base.base_page import BasePage
import utilities.custom_logger as cl
import logging
import time
import datetime
import random
from datetime import timedelta


class EventCreatePage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    get_started = "//a[@class='btn text--boldest btn-red btn-shadow padding--vert padding--hor text--20']"
    select_design = "//div[contains(@class,'container-event por bg--gray-lr container-bg')]//a[@href='/event/select-template-design/']"
    design_template = "//img[@title='invitation4.jpg']"
    event_title_field = "create_invitation_form_title"
    celebrants_name_field = "create_invitation_form_celebrants"
    hosted_field = "create_invitation_form_host"
    phone_number_field = "create_invitation_form_phone"
    event_date_field = "js-datepicker-eventDate"
    rsvp_field = "js-datepicker-rsvp"
    venue_address_field = "create_invitation_form_venue"
    city_field = "create_invitation_form_city"
    postcode_field = "create_invitation_form_code"
    continue_button = "create_invitation_form_continue"
    add_gift_link ="html/body/div/main/section[2]/div[2]/div/div/div[1]/a"
    gift_template = ".//*[@id='17']/div/div[1]/div[3]/a"
    select_gift_button = "//a[contains(@class,'btn btn-red')]"
    add_charity_button = "//img[@class='poa box-img-charity']"
    charity_template = ".//*[@id='js-templates-container']/div[1]/ul/li[4]/a/div/p"
    select_charity_button = "//a[contains(@class,'btn btn-red')]"
    invitation_card = "//div[@class='pull-left bg--white padding--20px invitation-card-img']"
    event_create_page_message = "//h3[contains(text(),'How much of your gift would you like to share with charity?')]"
    event_date = "//a[@class='ui-state-default'][contains(text(),'22')]"
    event_date_today = "//a[@class='ui-state-default ui-state-highlight ui-state-active']"
    time_dropdown = "//html//div[@class='row']//div[@class='row']//div[3]/div[1]/input[1]"
    start_time = "//li[@class='ui-timepicker-pm'][contains(text(),'23:00')]"
    end_time = "//li[@class='ui-timepicker-am'][contains(text(),'00:30')]"
    create_event_button = "//button[contains(text(),'Create event')]"
    safe_draft_button = "//button[contains(text(), 'Save draft')]"
    login_modal_link = "//a[contains(text(), 'Log in')]"
    today_date = datetime.datetime.today().strftime('%d/%m/%Y')
    ten_days_from_today = (datetime.datetime.now() + timedelta(days=10)).strftime('%d/%m/%Y')
    five_days_from_today = (datetime.datetime.now() + timedelta(days=5)).strftime('%d/%m/%Y')
    delete_button = "//tbody[contains(@class,'host-body')]//tr[1]//td[5]//span[1]//a[1]"
    user_icon = "//div[@class='pull-right']//button[@type='button']"
    confirm_delete_button = "//a[contains(@type,'submit')]"
    dropdown_arrow = "//span[@class = 'caret cl-red']"
    my_events = "//ul[@class='dropdown-menu']//a[@title='My events'][contains(text(),'My events')]"
    web_automation_test_locator = "Web Automation Test"
    logo_button = "//img[@src='/bundles/design/img/logo/kindergifts_logo_green.png']"
    random_int = random.randint(10000,99999)
    seven_num_rand = random.randint(1000000,9999999)
    log_out_css = "a[title='Log out']"
    event_random = "//span[@class='template-name cl-purple text-bold text--16'][contains(text(),'{}' )]"
    event_title_error_message = "//span[contains(text(), 'Please enter event title.')]"
    celebrant_name_error_message = "//span[@class='error'][contains(text(),'Please enter first and last name(s).')]"
    host_error_message = "//span[@class='error'][contains(text(),'Please enter host name.')]"
    date_error_message = "//span[@class='error'][contains(text(),'Please enter date.')]"
    rsvp_date_error_message = "//span[@class='error'][contains(text(),'Please enter RSVP date.')]"
    start_time_error_message = "//span[@class='error'][contains(text(),'Please enter start time.')]"
    end__time_error_message = "//span[@class='error'][contains(text(),'Please enter end time.')]"
    phone_number_error_message = "//span[@class='error'][contains(text(),'Phone number can contain only digits.')]"
    template = "//div[@class='pull-left bg--white padding--20px invitation-card-img']//img[@class='img-responsive template-image']"




    ############################
    ### Element Interactions ###
    ############################


    def click_get_started_button(self):
        self.element_click(self.get_started, locator_type="xpath")

    def click_select_design(self):
        self.element_click(self.select_design, locator_type="xpath")

    def choose_design_template(self):
        self.element_click(self.design_template, locator_type="xpath")

    def enter_event_title_field(self, event_title):
        self.send_keys(event_title, self.event_title_field)

    def enter_celebrant_name(self, celebrant_name):
        self.send_keys(celebrant_name, self.celebrants_name_field)

    def enter_host_name(self, host_name):
        self.send_keys(host_name, self.hosted_field)

    def enter_random_phone_number(self, phone_number=seven_num_rand):
        self.send_keys(phone_number, self.phone_number_field)

    def enter_phone_number(self, phone_number):
        self.send_keys(phone_number, self.phone_number_field)

    def enter_n_days_event_date(self, event_date=ten_days_from_today):
        self.send_keys(event_date, self.event_date_field)

    def enter_n_days_rsvp_date(self, rsvp_date=five_days_from_today):
        self.send_keys(rsvp_date, self.rsvp_field)

    def enter_event_date(self, event_date):
        self.send_keys(event_date, self.event_date_field)

    def enter_rsvp_date(self, rsvp_date):
        self.send_keys(rsvp_date, self.rsvp_field)

    def enter_venue_address(self, venue_address):
        self.send_keys(venue_address, self.venue_address_field)

    def enter_city_name(self, city_name):
        self.send_keys(city_name, self.city_field)

    def enter_postcode(self, postcode=random_int):
        self.send_keys(postcode, self.postcode_field)

    def click_continue_button(self):
        self.element_click(self.continue_button)

    def click_add_gift(self):
        self.element_click(self.add_gift_link, locator_type="xpath")

    def choose_gift(self):
        self.element_click(self.gift_template, locator_type="xpath")

    def press_select_gift_button(self):
        self.element_click(self.select_gift_button, locator_type="xpath")

    def press_add_charity_button(self):
        self.element_click(self.add_charity_button, locator_type="xpath")

    def choose_charity(self):
        self.element_click(self.charity_template, locator_type="xpath")

    def press_select_charity_button(self):
        self.element_click(self.select_charity_button, locator_type="xpath")

    def press_create_event_btn(self):
        self.element_click(self.create_event_button, locator_type="xpath")

    def press_save_draft_btn(self):
        self.element_click(self.safe_draft_button, locator_type="xpath")

    def press_login_modal_link(self):
        self.element_click(self.login_modal_link, locator_type="xpath")

    def click_delete_button(self):
        self.element_click(self.delete_button, locator_type="xpath")

    def click_confirm_delete_btn(self):
        self.element_click(self.confirm_delete_button, locator_type="xpath")

    def click_dropdown_arrow(self):
        self.element_click(self.dropdown_arrow, locator_type="xpath")

    def click_my_events(self):
        self.element_click(self.my_events, locator_type="xpath")

    def click_logo_button(self):
        self.element_click(self.logo_button, locator_type="xpath")

    def click_log_out(self):
        self.element_click(self.log_out_css, locator_type="css")

    def event_random_click(self, event_name):
        self.element_click(self.event_random.format(event_name), locator_type="xpath")

    def click_template(self):
        self.element_click(self.template, locator_type="xpath")

    def create_design(self, event_name="", event_title="", celebrant_name="",
                      host_name="", venue_address="", city_name=""):
        self.click_get_started_button()
        self.click_select_design()
        self.event_random_click(event_name)
        self.enter_event_title_field(event_title)
        self.enter_celebrant_name(celebrant_name)
        self.enter_host_name(host_name)
        self.scroll_browser(direction="down")
        self.enter_random_phone_number()
        self.enter_n_days_event_date()
        self.enter_n_days_rsvp_date()
        self.enter_venue_address(venue_address)
        self.enter_city_name(city_name)
        self.enter_postcode()
        self.click_continue_button()
        self.scroll_browser(direction="down")

    def add_gift(self):
        self.click_add_gift()
        self.choose_gift()
        self.press_select_gift_button()

    def add_charity(self):
        self.press_add_charity_button()
        self.choose_charity()
        self.press_select_charity_button()
        self.press_save_draft_btn()
        self.scroll_browser(direction="up")
        time.sleep(4)
        self.press_login_modal_link()

    def go_to_event_details_page(self):
        self.click_dropdown_arrow()
        self.click_my_events()

    def delete_event(self):
        self.click_delete_button()
        time.sleep(2)
        self.click_confirm_delete_btn()
        time.sleep(2)

    def log_out(self):
        self.click_dropdown_arrow()
        self.click_log_out()

    def verify_step_created_successfully(self):
        result = self.is_element_present(self.event_create_page_message, locator_type="xpath")
        return result

    def verify_event_created(self):
        result = self.is_element_present(self.web_automation_test_locator, locator_type="link")
        return result

    def verify_element_deleted_successfully(self):
        result = self.is_element_missing(self.web_automation_test_locator, locator_type="xpath")
        return result

    def check_error_messages(self):
        self.is_element_present(self.event_title_error_message, locator_type="xpath")
        self.is_element_present(self.celebrant_name_error_message, locator_type="xpath")
        self.is_element_present(self. host_error_message, locator_type="xpath")
        self.is_element_present(self.date_error_message, locator_type="xpath")
        self.is_element_present(self.rsvp_date_error_message, locator_type="xpath")
        self.is_element_present(self.start_time_error_message, locator_type="xpath")
        self.is_element_present(self.end__time_error_message, locator_type="xpath")
        self.is_element_present(self.phone_number_error_message, locator_type="xpath")

    def create_invalid_design(self, event_name="", event_title="", celebrant_name="",
                              host_name="", phone_number="", event_date="", rsvp_date="", venue_address="", city_name=""):
        self.click_get_started_button()
        self.click_select_design()
        self.event_random_click(event_name)
        self.enter_event_title_field(event_title)
        self.enter_celebrant_name(celebrant_name)
        self.enter_host_name(host_name)
        self.scroll_browser(direction="down")
        self.enter_phone_number(phone_number)
        self.enter_event_date(event_date)
        self.enter_rsvp_date(rsvp_date)
        self.enter_venue_address(venue_address)
        self.enter_city_name(city_name)
        self.enter_postcode()
        self.click_continue_button()
        self.scroll_browser(direction="down")

    def verify_invalid_event_failed(self):
        if self.driver.current_url is not "http://kindergifts-dev.etonlabs.com/event/web-automation/create":
            return True
        else:
            return False





























