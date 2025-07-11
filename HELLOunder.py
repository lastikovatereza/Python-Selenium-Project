import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test case 1: Positive LogIn test

# Open browser
driver = webdriver.Chrome()
time.sleep(3)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

# Type username student into Username field
username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

# Type password Password123 into Password field
password_locator = driver.find_element(By.NAME, "password")
password_locator.send_keys("Password123")

# Push Submit button
submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submit_button_locator.click()
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page

button_text = driver.find_element(By.LINK_TEXT, "Log out")

actual_button = button_text.text
assert actual_button == "Log out"
# my solution
assert button_text.is_displayed()
#russian guy solution


"""
THIS IS 
HOW I MAKE 
A HUUUGE 
COMMENT
"""