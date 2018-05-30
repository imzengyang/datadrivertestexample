import unittest
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://118.31.19.120:3000/')

    def tearDown(self):
        self.driver.quit()