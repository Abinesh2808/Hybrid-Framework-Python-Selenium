from selenium.webdriver import Chrome
import pytest
from selenium.webdriver import ChromeOptions
from Generic.Logs import *

op = ChromeOptions()
op.add_experimental_option("prefs",{"autofill.profile_enabled":False,"autofill.credit_card_enabled": False,
                                    "safebrowsing.enabled":True})
"""
Chrome was showing popup to save address and card informations so i have used this
"""

@pytest.fixture
def config():
    log("info", "Launching Browser")
    driver = Chrome(options=op)
    log("info", "Browser Launched")
    log("info", "Maximizing Browser")
    driver.maximize_window()
    log("info", "Browser Maximized")
    driver.implicitly_wait(5)
    log("info", "Entering URL")
    driver.get("https://demowebshop.tricentis.com/")
    log("info", "URL Entered")
    yield driver
    log("info", "Closing Browser")
    driver.quit()
    log("info","Browser Closed")

