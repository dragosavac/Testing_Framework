from pages.kindergifts.event_create_page import EventCreatePage
from pages.kindergifts.login_page import LoginPage
import pytest
import unittest
from utilities.test_status import TestStatus
import time
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class EventCreateTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.kindergifts = EventCreatePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)

    def setUp(self):
        self.kindergifts.click_logo_button()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/rade_dragosavac/PycharmProjects/framework/config_files/test_data.csv"))
    @unpack
    def test_valid_creating_event(self, event_name, event_title, celebrant, host, city, username, password):
        self.kindergifts.create_design(event_name, event_title, celebrant, host, city)
        result1 = self.kindergifts.verify_step_created_successfully()
        self.ts.mark(result1, "Design created successfully")
        self.kindergifts.add_gift()
        result2 = self.kindergifts.verify_step_created_successfully()
        self.ts.mark(result2, "Gift added successfully")
        self.kindergifts.add_charity()
        result3 = self.kindergifts.verify_step_created_successfully()
        self.ts.mark(result3, "Charity added successfully")
        time.sleep(2)
        self.lp.login(username, password)
        time.sleep(2)
        self.kindergifts.go_to_event_details_page()
        result4 = self.kindergifts.verify_event_created()
        self.ts.mark(result4, "Event created successfully")
        self.kindergifts.delete_event()
        result5 = self.kindergifts.verify_element_deleted_successfully()
        self.ts.mark_final("test_valid_creating_event", result5, "Event is deleted and Test -> Passed")
        self.kindergifts.log_out()
        time.sleep(2)

    @pytest.mark.run(order=2)
    @data(*getCSVData("/Users/rade_dragosavac/PycharmProjects/framework/config_files/invalid_test_data.csv"))
    @unpack
    def test_invalid_creating_event(self, event_name, event_title, celebrant,
                                    host, phone_number, event_date, rsvp_date):
        self.kindergifts.create_invalid_design(event_name, event_title, celebrant,
                                               host, phone_number, event_date, rsvp_date)
        self.kindergifts.check_error_messages()
        time.sleep(3)
        result1= self.kindergifts.verify_invalid_event_failed()
        self.ts.mark_final("Test", result1, "Invalid event is not created")





