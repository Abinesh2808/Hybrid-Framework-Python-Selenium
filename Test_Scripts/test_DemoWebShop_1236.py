import pytest

from POM.HomePage import *
from POM.LoginPage import *
from POM.OrderDetailsPage import *
from POM.AccountPage import *
from Generic.Verify_Title import *
from Generic.ReadingExcel import *

test_data = read_testdata("Testdata")
titles = read_testdata("Titles")
messages = read_testdata("Messages")

# @pytest.mark.skip
def test_demowebshop_1236(config):
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
    home.orders_link()
    verify_title(driver,titles["Accountpage"])
    acnt = AccountPage(driver)
    acnt.order_details(f"{acnt.get_onum()}")
    verify_title(driver,titles["Orderdetailspage"])
    order = OrderDetailsPage(driver)
    order.download_invoice()
    order.verify_download(f"order_{acnt.get_onum()}.pdf")
    home.logout_link()
    verify_title(driver, titles["Homepage"])
