from Generic.Logs import *
from Generic.Screenshot import *

class AccountPage:
    def __init__(self,driver):
        self.driver = driver

    def get_onum(self):
        with open("D:\ordernumber.txt","r") as obj:
            onum = obj.readline().split(": ")
            return onum[1]

    def order_details(self,num):
        try:
            log("info", "Selecting Specified Order Details")
            self.driver.find_element("xpath",f"(//strong[.='Order Number: {num}']/../../div)[2]").click()
            log("info", "Specified Order Selected")
        except:
            log("error", "Invalid Order Number")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Invalid Order Number")


"""
if there is multiple orders present, we cant inspect details button. so xpath by traversing used
means, using order number traverse to common parent then traverse to details button 
"""

