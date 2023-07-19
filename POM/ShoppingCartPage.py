from Generic.ReadingExcel import *
from Generic.Wrappers import *
from Generic.Logs import *

loc = read_locator("ShoppingCartPage")
class ShoppingCartPage:
    def __init__(self,driver):
        self.driver = driver

    def terms_and_conditions(self):
        log("info", "Clicking Terms and Conditions")
        click_element(loc["Terms Of Service"],self.driver)
        log("info", "Terms and Conditions Clicked")

    def checkout_button(self):
        log("info", "Clicking Checkout Button")
        click_element(loc["Checkout button"],self.driver)
        log("info", "Checkout Button Clicked")