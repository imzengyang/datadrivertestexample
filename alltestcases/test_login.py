# coding=utf-8

import unittest
from HTMLReport import AddImage

from ddt import ddt,data,unpack,file_data
from common.create_driver import getDriver
from common.manage_dir import getPngfileName
import os
import time
import csv

def get_data_csv(filename):
    users = []
    with open(filename,'r',encoding='UTF-8') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            users.append(row)
    return users


@ddt
class UserActionTest(unittest.TestCase):
    driver =  getDriver()
    
    
    def setUp(self):
        self.driver.maximize_window()
        self.driver.get('http://118.31.19.120:3000/')

    def tearDown(self):
        print(getPngfileName())
        base64Img = self.driver.get_screenshot_as_base64()
        AddImage(base64Img)
        self.driver.save_screenshot(getPngfileName())
        self.driver.delete_all_cookies()

    @classmethod
    def setUpClass(cls):
        cls.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @data(*get_data_csv('./testdata/userlogin.csv'))
    @unpack
    def test_login(self,username,password,excpetStatus,checkpoint):

        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('name').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(password)
        self.driver.find_element_by_id('pass').submit()
        okurl = self.driver.current_url

        self.assertEqual(okurl,'http://118.31.19.120:3000/')

        loginName = self.driver.find_element_by_css_selector('#sidebar > div:nth-child(1) > div.inner > div > div > span.user_name > a').text
        self.assertEqual(loginName,'testuser3')

    # def test_register(self):
    #     self.driver.find_element_by_link_text('注册').click()
    #     self.driver.get('http://118.31.19.120:3000/signup')
    #     self.driver.find_element_by_id('loginname').send_keys('testuser3')
    #     self.driver.find_element_by_id('pass').send_keys('123456')
    #     self.driver.find_element_by_id('re_pass').send_keys("123456")
    #     self.driver.find_element_by_id('email').send_keys('123456@123.com')
    #     self.driver.find_element_by_id('pass').submit()
        

if __name__ == "__main__":
    unittest.main()
