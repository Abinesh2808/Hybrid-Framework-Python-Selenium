from Generic.Wrappers import *
from Generic.ReadData import read_locator
from Generic.Logs import *

loc = read_locator("LoginPage")
class Loginpage:
    def __init__(self,driver):
        self.driver = driver

    def email(self,mail):
        log("info", "Entering Email")
        enter_data(loc["Email"],mail,self.driver)
        log("info", "Email Entered")

    def password(self,pwd):
        log("info", "Entering Password")
        enter_data(loc["Password"],pwd,self.driver)
        log("info", "Password Entered")

    def login_button(self):
        log("info", "Clicking Login Button")
        click_element(loc["Login Button"],self.driver)
        log("info", "Login Button Clicked")
