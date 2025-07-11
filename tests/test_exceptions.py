import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_object.exceptions_page import ExceptionsPage


@pytest.mark.exceptions
@pytest.mark.homework
class TestExceptions:
    def test_exceptions(self, driver):
        #driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        exceptions_page = ExceptionsPage(driver)
        exceptions_page.open()

        #add_button = driver.find_element(By. ID, "add_btn")
        #add_button.click()
        exceptions_page.add_second_row()
# in the fixture (conftest page) there is a (my_driver.implicitly_wait(10)) which will make the test wait for the webdriver to
# show the second row --- continuing at the end of the page viz row2locator for implicit wait

        #wait = WebDriverWait(driver, 10)
        #row2input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))
        #assert row2input_element.is_displayed()
# this is the explicit wait ^^


        row2locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        #assert row2locator._is_displayed(), "Row 2 input should be displayed but it is not."
        # if we have a class attribute for more than one element we can put the path into brackets ()
        # and add [] with the number of needed element

        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed but it is not."
