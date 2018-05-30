import unittest

from po.homepage import HomePage
from po.loginpage import LoginPage
from basecase import BaseTestCase


class LonginTest(BaseTestCase):

    def test_login(self):
        homepage = HomePage(self.driver)
        homepage.gotoLogin_page(self.driver)
        loginpg = LoginPage(self.driver)
        loginpg.user_login(self.driver,"xxxxxx",'ssssssss')
        assertEquals(loginpg.error_msg,"用户名或密码错误")
