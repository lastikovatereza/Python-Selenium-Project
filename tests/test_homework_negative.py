import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHomeworkNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.homework
    @pytest.mark.negative
    def test_homework(self):
        driver = webdriver.Chrome()
        # it can be removed by using fixture, example test login negative
        driver.get("https://practicetestautomation.com/practice-test-login/")

#Type username student into Username field
        username_locators = driver.find_element(By.ID, "username")
        username_locators.send_keys("student")
#Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID,"password")
        password_locator.send_keys("sdasdasdsad")
#Push Submit button
        submit_button_locators = driver.find_element(By.ID, "submit")
        submit_button_locators.click()
#Verify error message is displayed
        error_message = driver.find_element(By.ID, "error")
        error_message.is_displayed(), "Error message is not displayed but it should."
#Verify error message text is Your password is invalid!
        error_message = error_message.text
        assert error_message == "Your password is invalid!", "Error password is not invalid but it should."
