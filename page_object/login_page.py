from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_object.base_page import BasePage


class LoginPage(BasePage):
    #we can inherit attributes from other class (superclass) to another (subclass)
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By. ID, "username")
    __password_field = (By. NAME, "password")
    __submit_button = (By. XPATH, "//button[@class='btn']")
    __error_message = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        #self._driver = driver
        super().__init__(driver)

    def open(self):
        #self._driver.get(self.__url)
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_button)

    def get_error_message(self) -> str:
        return super()._get_text(self.__error_message, time=3)

"""
        wait = WebDriverWait(self._driver, 10)
        wait.until(ec.visibility_of_element_located(self.__username_field))
        self._driver.find_element(self.__username_field).send_keys(username)
        wait.until(ec.visibility_of_element_located(self.__password_field))
        self._driver.find_element(self.__password_field).send_keys(password)
        wait.until(ec.visibility_of_element_located(self.__submit_button))
        self._driver.find_element(self.__submit_button).click()
"""



