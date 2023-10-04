from Generic.ReadData import *
from Generic.Wrappers import *
from Generic.Verify_Message import *
from Generic.Logs import *

loc = read_locator("ContactUsPage")

class ContactUsPage:
    def __init__(self,driver):
        self.driver = driver

    def verify_name(self,name):
        log("info", "Verifying Name in the Name Textfield")
        ele = self.driver.find_element(*loc["Verify Name"]).get_attribute('value')
        assert ele == name, "Name not Matches" and log("info", "Name not Matches")
        log("info", "Name Verified")

    def verify_email(self,mail):
        log("info", "Verifying Email in the Email Textfield")
        ele = self.driver.find_element(*loc["Verify Email"]).get_attribute('value')
        assert ele == mail, "Email not matches" and log("info", "Email not Matches")
        log("info", "Email Verified")

    def add_enquiry(self,enquiry):
        log("info", "Entering Enquiry")
        enter_data(loc["Enter Enquiry"],enquiry,self.driver)
        log("info", "Enquiry Entered")

    def submit_button(self):
        log("info", "Clicking Submit Button")
        click_element(loc["Submit"],self.driver)
        log("info", "Submit Button Clicked")

    def verify_enquiry_message(self,msg):
        address = loc["Enquiry Sent Message"]
        verify_message(self.driver,address,msg)


