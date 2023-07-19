from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Generic.Screenshot import *
from Generic.Logs import *

def verify_message(driver,loc,message):
    try:
        wait = WebDriverWait(driver,5)
        log("info", "Verifying Message")
        wait.until(ec.text_to_be_present_in_element(loc,message))
        log("info", "Message Verified")
    except:
        log("error", "No Message Displayed")
        log("info", "Taking Screenshot")
        take_screenshot(driver)
        log("info", "Screenshot Captured")
        raise Exception ("Message not Displayed")