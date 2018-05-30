
from po.base import BasePage
from po.base import InvalidPageException

class LoginPage(BasePage):

    _login_view_locator = ".active"
    _login_name_selector = "#name"
    _login_passwd_selector = "#pass"

    _login_btn_selector = ".span-primary"

    _login_error_msg_selector='.alert strong'

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def user_login(self,username,passwd):
        self.driver.find_element_by_css_selector(self._login_name_selector).send_keys(username)
        self.driver.find_element_by_css_selector(self._login_passwd_selector).send_keys(passwd)
        self.driver.find_element_by_css_selector(self._login_btn_selector).click()


    @property
    def error_msg(self):
        return self.driver.find_element_by_css_selector(self._login_error_msg_selector).text.strip()

    # def _validate_page(self, driver):
    #     try:
    #         driver.find_element_by_css_selector(self._product_view_locator).text 
    #     except:
    #         raise InvalidPageException('login page not loaded')