from pages.kindergifts.login_page import LoginPage
import pytest
import unittest
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.click_login_link()
        self.lp.login("rade.dragosavac@etondigital.com", "sn1987aba")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.click_login_link()
        self.lp.login("test@email.com", "hgf65")
        result = self.lp.verify_login_failed()
        self.ts.mark(result, "Login Failed")




