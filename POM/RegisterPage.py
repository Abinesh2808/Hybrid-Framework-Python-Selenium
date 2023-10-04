from Generic.Wrappers import *
from Generic.ReadData import *
from Generic.Verify_Message import *
from Generic.Logs import *

loc = read_locator("RegisterPage")

class RegisterPage:
    def __init__(self,driver):
        self.driver = driver

    def gender(self,gend):
        try:
            log("info", "Clicking Specified Gender")
            self.driver.find_element("xpath",f"//input[@id='gender-{gend}']").click()
            log("info", "Specified Gender Clicked")
        except:
            log("error", "Invalid Gender")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Invalid Gender")

    def first_name(self,fn):
        log("info", "Entering First Name")
        enter_data(loc["FirstName"],fn,self.driver)
        log("info", "First Name Entered")

    def last_name(self,ln):
        log("info", "Entering Last Name")
        enter_data(loc["LastName"],ln,self.driver)
        log("info", "Last Name Entered")

    def email(self,mail):
        log("info", "Entering Email")
        enter_data(loc["Email"],mail,self.driver)
        log("info", "Email Entered")

    def password(self,pwd):
        log("info", "Entering Password")
        enter_data(loc["Password"],pwd,self.driver)
        log("info", "Password Entered")

    def confirm_password(self,cpwd):
        log("info", "Entering Confirm Password")
        enter_data(loc["Confirm Password"],cpwd,self.driver)
        log("info", "Confirm Password Entered")

    def register_button(self):
        log("info", "Clicking Register Button")
        click_element(loc["Register Button"],self.driver)
        log("info", "Register Button Clicked")

    def verify_register_message(self,msg):
        verify_message(self.driver,loc["Verify Message"],msg)

    def continue_button(self):
        log("info", "Clicking Continue Button")
        click_element(loc["Continue Button"],self.driver)
        log("info", "Continue Button Clicked")





