import unittest
from alltestcases.test_login import UserActionTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(UserActionTest('test_login'))
    suite.addTest(UserActionTest('test_register'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())