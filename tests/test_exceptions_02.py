import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.mark.exceptions
@pytest.mark.homework
@pytest.mark.exceptions2

class TestExceptions02:
    def test_element_not_interactable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element(By. ID, "add_btn")
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row2element = wait.until(ec.presence_of_element_located((By. XPATH, "//div[@id='row2']/input")))
        row2element.send_keys("Pasta")
        # save_button_locator = driver.find_element(By. NAME, "Save")
        driver.find_element(By. XPATH, "//div[@id='row2']/button[@name='Save']").click()

        verify_text_save = wait.until(ec.visibility_of_element_located((By. ID, "confirmation")))
        # verify_text_save = driver.find_element(By. ID, "confirmation")
        actual_verify_text = verify_text_save.text
        assert actual_verify_text == "Row 2 was saved", "Confirmation message is not expected."

@pytest.mark.homework
@pytest.mark.exceptions
@pytest.mark.exceptions3
class TestExceptions03:
    def test_invalid_element_state_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        edit_button = driver.find_element(By.ID, "edit_btn")
        edit_button.click()
        row1 = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        previous_text = row1.text
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row1))
        row1.clear()
        row1.send_keys("Mango")
        add_button = driver.find_element(By. XPATH, "//div[@id='row1']/button[@id='add_btn']")
        add_button.click()

        row2 = wait.until(ec.presence_of_element_located((By. XPATH, "//div[@id='row2']")))
        # actual_text = row1.text
        assert previous_text != "Mango", "The text did not change but it should have."
        text = row1.get_attribute("value")
        assert text == "Mango", "The text did not change but it should have got" + text

@pytest.mark.exceptions4
@pytest.mark.exceptions
@pytest.mark.homework
class TestExceptions04:
    def test_stale_element_reference_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        instructions_text = driver.find_element(By. ID, "instructions")
        instructions_text.is_displayed()
        add_button = driver.find_element(By.XPATH, "//div[@id='row1']/button[@id='add_btn']")
        add_button.click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By. ID, "instructions"))), "instructions text element should not be displayed"
        # assert not instructions_text.is_displayed(), "instructions text element should not be displayed"
        # assert instructions_text.is_displayed() == False
        # last two solutions give us error of element not existing idk


@pytest.mark.exceptions5
@pytest.mark.homework
class TestExceptions05:
    def test_timeout_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_2 = driver.find_element(By. ID, "add_btn")
        add_button_2.click()
        wait = WebDriverWait(driver, 3)
        wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")), "Row 2 is not displayed."), "another message"
        row2 = driver.find_element(By.XPATH, "//div[@id='row2']/input")._is_displayed(), "Row 2 is not displayed."



