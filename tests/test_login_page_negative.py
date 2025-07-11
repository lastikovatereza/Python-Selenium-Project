import time

import pytest

from selenium.webdriver.common.by import By

from page_object.login_page import LoginPage


class TestNegativeScenarios:
    # always have TEST in the name !!!!

    # new selenium test
    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("fheudsfhdskfhds", "Password123", "Your username is invalid!"),
                              ("student", "sdasdasdsad", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # fixed function, no need to specify driver
        # Test case 2: Negative username test

        login_page = LoginPage(driver)

        login_page.open()

        login_page.execute_login(username, password)

        time.sleep(2)

        assert login_page.get_error_message() == expected_error_message, "Error message is not expected."

        # Open page

        #driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        #username_locator = driver.find_element(By.ID, "username")
        #username_locator.send_keys(username)
        # username_locator.send_keys("student")
        # Type password Password123 into Password field
        #password_locator = driver.find_element(By.NAME, "password")
        #password_locator.send_keys(password)
        # Push Submit button
        #submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        #submit_button_locator.click()
        #time.sleep(2)

        # Verify error message is displayed
        #error_message_locator = driver.find_element(By.ID, "error")
        #assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be."
        # Verify error message text is Your username is invalid!
        #actual_message = error_message_locator.text
        #assert actual_message == expected_error_message, "Error message is not expected."

#this can be deleted and it will still work because of parameters
    """
    def test_homework(self, driver, username, password, expected_error_message):
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username student into Username field
        username_locators = driver.find_element(By.ID, "username")
        username_locators.send_keys(username)
        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)
        # Push Submit button
        submit_button_locators = driver.find_element(By.ID, "submit")
        submit_button_locators.click()
        # Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        error_message.is_displayed(), "Error message is not displayed but it should."
        # Verify error message text is Your password is invalid!
        error_message = error_message.text
        assert error_message == expected_error_message, "Error password is not invalid but it should."
"""

"""
    # beginning of learning selenium
    def test_negative_username(self, driver):
        # fixed function, no need to specify driver
        # Test case 2: Negative username test
        # Open page

        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("fheudsfhdskfhds")
        #username_locator.send_keys("student")
        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")
        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)
        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should be."
        # Verify error message text is Your username is invalid!
        actual_message = error_message_locator.text
        assert actual_message == "Your username is invalid!", "Error message is not expected."
"""
