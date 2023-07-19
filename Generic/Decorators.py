from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Generic.Screenshot import *
from Generic.Logs import *
def verify_element(func):
    def inner(*args,**kwargs):
        try:
            wait = WebDriverWait(args[-1],5)
            log("info", "Verifying Element in DOM")
            wait.until(ec.visibility_of_element_located(args[0]))
            func(*args,**kwargs)
            log("info", "Element Verified")
        except:
            log("error", "Element Not Present")
            log("info", "Taking Screenshot")
            take_screenshot(args[-1])
            log("info", "Screenshot Captured")
            raise Exception ("No Such Element Located")
    return inner

