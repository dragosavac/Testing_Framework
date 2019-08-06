from pages.courses.register_course_page import RegisterCoursePage
from utilities.test_status import TestStatus
from pages.home.login_page import LoginPage
import unittest
import pytest
from ddt import ddt, data, unpack
import time
from pages.home.navigation_page import NavigationPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCourseTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)
        self.nav = NavigationPage(self.driver)

    def set_up(self):
        self.nav.navigate_to_all_courses()



    @pytest.mark.run(order = 1)
    @data (("JavaScript for beginners", "10", "1220", "10"), ("Learn Python 3 from scratch", "20", "1220", "20"))
    @unpack
    def test_invalid_enrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.lp.login("test@email.com", "abcabc")
        self.courses.enter_search_field(courseName)
        self.courses.click_search_button()
        self.courses.select_course()
        time.sleep(4)
        self.courses.enroll_course(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result,
                           "Enrollment Verification")
        self.courses.click_all_courses_link()




