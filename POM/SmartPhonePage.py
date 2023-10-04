from Generic.ReadData import *
from Generic.Wrappers import *
from Generic.Verify_Message import *
from Generic.Logs import *

loc = read_locator("SmartPhonePage")

class SmartPhonePage:
    def __init__(self,driver):
        self.driver = driver

    def quantity(self,qty):
        log("info", "Clearing Default Quantity")
        clear_element(loc["Quantity"],self.driver)
        log("info", "Entering Specified Quantity")
        enter_data(loc["Quantity"],qty,self.driver)
        log("info", "Specified Quantity Entered")

    def add_to_cart(self):
        log("info", "Clicking Add to Cart Button")
        click_element(loc["Add to Cart"],self.driver)
        log("info", "Add to Cart Button Clicked")

    def verify_product_added_to_cart_message(self,msg):
        address = loc["Product Added Message"]
        verify_message(self.driver,address,msg)

    def verify_cart_count(self,qty):
        verify_message(self.driver,loc["Cart Count"],f"({qty})")

    def shopping_cart(self):
        log("info", "Clicking Shopping Cart Link")
        click_element(loc["Cart Link"],self.driver)
        log("info", "Shopping Cart Link Clicked")

    def add_review(self):
        log("info", "Clicking Add Review Link")
        click_element(loc["Add Review"],self.driver)
        log("info", "Add Review Link Clicked")


