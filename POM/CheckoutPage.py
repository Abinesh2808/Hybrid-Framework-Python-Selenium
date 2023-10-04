from Generic.Wrappers import *
from Generic.ReadData import *
from selenium.webdriver.support.select import Select
from Generic.Verify_Message import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Generic.Logs import *
from Generic.Screenshot import *

loc = read_locator("CheckOutPage")
order_num = None

class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    def country(self,country_name):
        try:
            log("info", "Selecting Country from Drop-Down using Visible text")
            dd_add = self.driver.find_element(*loc["Country DD"])
            dd = Select(dd_add)
            dd.select_by_visible_text(country_name)
            log("info", "Country Name Selected from Drop-Down")
        except:
            log("error", "Invalid Country Name")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Invalid Country Name")

    def city(self,city_name):
        log("info", "Entering City Name")
        enter_data(loc["City"],city_name,self.driver)
        log("info", "City Name Entered")

    def address1(self,address):
        log("info", "Entering Address1")
        enter_data(loc["Address1"],address,self.driver)
        log("info", "Address1 Entered")

    def zip_code(self,zipcode):
        log("info", "Entering Zip Code")
        enter_data(loc["Zip Code"],zipcode,self.driver)
        log("info", "Zip Code Entered")

    def phone_number(self,phone):
        log("info", "Entering Phone Number")
        enter_data(loc["Phone Number"],phone,self.driver)
        log("info", "Phone Number Entered")

    def billing_address_continue(self):
        log("info", "Clicking Continue Button")
        click_element(loc["Billing Address Continue"],self.driver)
        log("info", "Continue Button Clicked")

    def shipping_address_continue(self):
        log("info", "Clicking Continue Button")
        click_element(loc["Shipping Address Continue"],self.driver)
        log("info", "Continue Button Clicked")

    def next_day_shipping_method(self):
        log("info", "Clicking Nexy Day Air (0.00) Shipping Method")
        click_element(loc["Next Day Air (0.00)"],self.driver)
        log("info", "Nexy Day Air (0.00) Shipping Method Clicked")

    def shipping_method_continue(self):
        log("info", "Clicking Continue Button")
        click_element(loc["Shipping Method Continue"],self.driver)
        log("info", "Continue Button Clicked")

    def credit_card(self):
        log("info", "Clicking Credit Card")
        click_element(loc["Credit Card"],self.driver)
        log("info", "Credit Card Clicked")

    def payment_method_continue(self):
        log("info", "Clicking Continue Button")
        click_element(loc["Payment Method Continue"],self.driver)
        log("info", "Continue Button Clicked")

    def credit_card_type(self,cc_type):
        try:
            log("info", "Selecting Mastercard from Drop-Down using Visible text")
            dd_add = self.driver.find_element(*loc["Credit Card Type DD"])
            dd = Select(dd_add)
            dd.select_by_visible_text(cc_type)
            log("info", "Mastercard Selected from Drop-Down")
        except:
            log("error", "Invalid Credit Card Type")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Invalid Credit Card Type")

    def card_holder_name(self,name):
        log("info", "Entering Card Holder Name")
        enter_data(loc["Card Holder Name"],name,self.driver)
        log("info", "Card Holder Name Entered")

    def card_number(self,num):
        log("info", "Entering Card Number")
        enter_data(loc["Card Number"],num,self.driver)
        log("info", "Card Number Entered")

    def expiry_month(self,month):
        try:
            log("info", "Selecting Expiry Month from Drop-Down using Visible text")
            dd_add = self.driver.find_element(*loc["Expiry Month DD"])
            dd = Select(dd_add)
            dd.select_by_visible_text(month)
            log("info", "Expiry Month Selected from Drop-Down")
        except:
            log("error", "Invalid Expiry Month")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Invalid Expiry Month")

    def expiry_year(self,year):
        try:
            log("info", "Selecting Expiry Year from Drop-Down using Visible text")
            dd_add = self.driver.find_element(*loc["Expiry Year DD"])
            dd = Select(dd_add)
            dd.select_by_visible_text(year)
            log("info", "Expiry Year Selected from Drop-Down")
        except:
            log("error", "Invalid Expiry Year")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Invalid Expiry Year")

    def car_code(self,code):
        log("info", "Entering Card Code")
        enter_data(loc["Card Code"],code,self.driver)
        log("info", "Card Code Entered")

    def payment_information_continue(self):
        log("info", "Clicking Continue Button")
        click_element(loc["Payment Information Continue"],self.driver)
        log("info", "Continue Button Clicked")

    def confirm_button(self):
        log("info", "Clicking Confirm Button")
        click_element(loc["Confirm Button"],self.driver)
        log("info", "Confirm Button Clicked")

    def verify_order(self,msg):
        address = loc["Order Successfully Placed Message"]
        verify_message(self.driver,address,msg)

    def verify_order_number(self):
        global order_num
        try:
            address = self.driver.find_element(*loc["Order Number"])
            wait = WebDriverWait(self.driver,5)
            log("info", "Verifying Order Number")
            wait.until(ec.visibility_of(address))
            log("info", "Order Number Verified")

            ele = self.driver.find_element("xpath","(//ul[@class='details']/li)[1]")
            order_num = ele.text

        except:
            log("error", "Order Number Not Displayed")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Order Number not Displayed")



