from Generic.ReadingExcel import *
from Generic.Wrappers import *
from selenium.webdriver.common.action_chains import ActionChains
from Generic.Screenshot import *
from Generic.Logs import *

loc = read_locator("HomePage")

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def register_link(self):
        log("info", "Clicking Register Link")
        click_element(loc["Register Link"],self.driver)
        log("info", "Register Link Clicked")

    def logout_link(self):
        log("info", "Clicking Logout Link")
        click_element(loc["Logout Link"],self.driver)
        log("info", "Logout Link Clicked")

    def login_link(self):
        log("info", "Clicking Login Link")
        click_element(loc["Login Link"],self.driver)
        log("info", "Login Link Clicked")

    def mouse_hover_electronics(self):
        try:
            ele = self.driver.find_element(*loc["Electronics"])
            a = ActionChains(self.driver)
            log("info","Mouse Horeing to the Specified Element")
            a.move_to_element(ele).perform()
        except:
            log("error", "Element Not Present")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Element Not Present")
    def cell_phones(self):
        log("info", "Clicking Cell Phones")
        click_element(loc["Cell Phones"],self.driver)
        log("info", "Cell Phones Clicked")

    def orders_link(self):
        try:
            lctn = self.driver.find_element(*loc["Orders Link"]).location
            log("info", "Scrolling Down to Specified Element")
            self.driver.execute_script(f"window.scrollBy({lctn['x']},{lctn['y']})")
            log("info", "Clicking Orders Link")
            click_element(loc["Orders Link"],self.driver)
            log("info", "Orders Link Clicked")
        except:
            log("error", "Element Not Present")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Element Not Present")

    def contact_us_link(self):
        try:
            lctn = self.driver.find_element(*loc["Contact Us Link"]).location
            self.driver.execute_script(f"window.scrollBy({lctn['x']},{lctn['y']})")
            log("info", "Clicking Contact Us Link")
            click_element(loc["Contact Us Link"],self.driver)
            log("info", "Contact Us Link Clicked")
        except:
            log("error", "Element Not Present")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Element Not Present")