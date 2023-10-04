import pytest
from POM.HomePage import *
from POM.LoginPage import *
from POM.ContactUsPage import *
from Generic.Verify_Title import *
from Generic.ReadData import *

test_data = read_testdata("Testdata")
titles = read_testdata("Titles")
messages = read_testdata("Messages")

# @pytest.mark.skip
def test_demowebshop_1238(config):
    driver = config
    verify_title(driver,titles["Homepage"])
    home = HomePage(driver)
    home.login_link()
    verify_title(driver,titles["Loginpage"])
    login = Loginpage(driver)
    login.email(test_data["Email"])
    login.password(test_data["Password"])
    login.login_button()
    verify_title(driver,titles["Homepage"])
    home.contact_us_link()
    verify_title(driver,titles["Contactuspage"])
    contact = ContactUsPage(driver)
    contact.verify_name(f"{test_data['Firstname']} "+f"{test_data['Lastname']}")
    contact.verify_email(test_data["Email"])
    contact.add_enquiry(test_data["Enquiry"])
    contact.submit_button()
    verify_title(driver,titles["Contactuspage"])
    contact.verify_enquiry_message(messages["Enquiry Sent"])
    home.logout_link()
    verify_title(driver,titles["Homepage"])