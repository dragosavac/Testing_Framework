from pages.kindergifts.register_page import RegisterPage
import pytest
import unittest
from utilities.test_status import TestStatus
import time



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.rp = RegisterPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=4)
    def test_valid_registration(self):
        self.rp.register("Rade", self.rp.random_user, "sn1987aba")
        result = self.rp.verify_registration_passed()
        time.sleep(3)
        self.ts.mark_final("Test Successful", result, "Registration completed")

    @pytest.mark.run(order=3)
    def test_already_reg_registration(self):
        self.rp.register("Rade", "rade.dragosavac@etondigital.com", "sn1987aba")
        result = self.rp.verify_already_reg_user()
        self.ts.mark(result, "Registration with already registered user is not possible")

    @pytest.mark.run(order=2)
    def test_invalid_registration(self):
        self.rp.register("Radojica", "szdfsdfsdf", "123")
        result = self.rp.verify_invalid_error_messages()
        self.ts.mark(result, "Registration with invalid credentials is not possible")

    @pytest.mark.run(order=1)
    def test_empty_registration(self):
        self.rp.register("", "", "")
        result = self.rp.verify_empty_error_messages()
        self.ts.mark(result, "Registration with empty fields is not possible")



