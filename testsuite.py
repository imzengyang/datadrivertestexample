import unittest
# from alltestcases.test_login import UserActionTest
from alltestcases.loginTest import LonginTest

def suite():
    suite = unittest.TestSuite()
    # loader = unittest.TestLoader().loadTestsFromTestCase(UserActionTest)
    # suite = unittest.TestSuite(loader)
    suite.addTest(LonginTest('test_login'))
    # suite.addTest(UserActionTest('test_register'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())