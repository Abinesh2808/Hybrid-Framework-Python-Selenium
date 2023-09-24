from POM.HomePage import *
from POM.RegisterPage import *
from POM.LoginPage import *
from Generic.Verify_Title import *
from Generic.ReadingExcel import *
import pytest

test_data = read_testdata("Testdata")
titles = read_testdata("Titles")
messages = read_testdata("Messages")


def test_wemowebshop_1234(config):
    driver = config
    verify_title(driver,titles["Homepage"])
    home = HomePage(driver)
    home.register_link()
    verify_title(driver,titles["Registerpage"])
    register = RegisterPage(driver)
    register.gender(test_data["Gender"])
    register.first_name(test_data["Firstname"])
    register.last_name(test_data["Lastname"])
    register.email(test_data["Email"])
    register.password(test_data["Password"])
    register.confirm_password(test_data["Password"])
    register.register_button()
    register.verify_register_message(messages["Registration Complete"])
    register.continue_button()
    verify_title(driver,titles["Homepage"])
    home.logout_link()
    verify_title(driver,titles["Homepage"])
    home.login_link()
    verify_title(driver,titles["Loginpage"])
    login = Loginpage(driver)
    login.email(test_data["Email"])
    login.password(test_data["Password"])
    login.login_button()
    verify_title(driver,titles["Homepage"])
    home.logout_link()
    verify_title(driver,titles["Homepage"])
