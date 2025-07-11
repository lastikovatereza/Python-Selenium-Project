from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_object.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        #self._driver = driver
        super().__init__(driver)

    #@property
    #def current_url(self) -> str:
        #super().current_url(self._driver.current_url)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator) #driver.find_element(self.__header_locator).text

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_button_locator) #self._driver.find_element(self.__log_out_button_locator).is_displayed()





