import unittest
from tests.kindergifts.login_test import LoginTests
from tests.kindergifts.event_create_test import EventCreateTest
from tests.kindergifts.register_test import RegisterTest

# Get all tests from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(EventCreateTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(RegisterTest)


# Create a test suite combining all test classes

smoke_test = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smoke_test)


