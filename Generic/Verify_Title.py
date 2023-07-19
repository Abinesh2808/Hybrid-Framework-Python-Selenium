from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Generic.Screenshot import take_screenshot
from Generic.Logs import *

def verify_title(driver,exp_title):
    try:
        wait = WebDriverWait(driver,5)
        log("info", "Verifying Title")
        wait.until(ec.title_is(exp_title))
        log("info", "Title Verified")
    except:
        log("error", "Title Not matches")
        log("info", "Taking Screenshot")
        take_screenshot(driver)
        log("info", "Screenshot Captured")
        raise Exception ("Title Not Matches")
