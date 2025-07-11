import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# @pytest.fixture(params=["chrome", "edge"])
@pytest.fixture
# if we want to execute tests in more browsers at the same time we use params in fixture brackets (like parameters)
def driver(request):
    browser = request.config.getoption("--browser")
    #getoption is for choosing a specific browser from the configuration
    # browser = request.param    #only one PARAM !!!!
    print(f"Creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "edge":
        my_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'edge' but got {browser}.")
    #my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} driver")
    my_driver.quit()
    # close is closing only one tab, quit is closing the whole browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )
