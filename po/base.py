from abc import abstractclassmethod

class BasePage(object):

    def __init__(self,driver):
        self._validate_page(driver)
        self.driver = driver

    
    @abstractmethod
    def _validate_page(self, driver):
        return


class InvalidPageException(Exception):
    """ Throw this exception when you don't find
         the correct page """
    pass