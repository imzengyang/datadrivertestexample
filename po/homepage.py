from po.base import BasePage
from po.base import InvalidPageException

class HomePage(BasePage):
    _home_login_link_selector = '登录'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
    

    def gotoLogin_page(self):
        return self.driver.find_element_by_link_text(self._home_login_link_selector).click()

    def _validate_page(self, driver):
        try:
            driver.find_element_by_link_text(self._home_login_link_selector)
        except:
            raise InvalidPageException("首页加载失败")
    
