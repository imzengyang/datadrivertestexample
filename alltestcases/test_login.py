

import unittest

from common.create_driver import getDriver

class UserActionTest(unittest.TestCase):

    def test_login(self):
        driver = getDriver()
        driver.get('http://118.31.19.120:3000/signin')
        driver.find_element_by_id('name').send_keys('testuser3')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_id('pass').submit()
        okurl =  driver.current_url

        self.assertEqual(okurl,'http://118.31.19.120:3000/')

        loginName = driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text

        self.assertEqual(loginName,'testuser3')

    # def test_register(self):
    #     driver = webdriver.Chrome()
    #     driver.get('http://118.31.19.120:3000/signup')
    #     driver.find_element_by_id('loginname').send_keys('testuser3')
    #     driver.find_element_by_id('pass').send_keys('123456')
    #     driver.find_element_by_id('re_pass').send_keys("123456")
    #     driver.find_element_by_id('email').send_keys('123456@123.com')
    #     driver.find_element_by_id('pass').submit()
        

if __name__ == "__main__":
    unittest.main()
