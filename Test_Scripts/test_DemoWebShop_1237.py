import pytest

from POM.HomePage import *
from POM.LoginPage import *
from POM.OrderDetailsPage import *
from POM.AccountPage import *
from POM.SmartPhonePage import *
from POM.ProductReviewsPage import *
from Generic.Verify_Title import *
from Generic.ReadData import *
import importlib, POM.CheckoutPage

importlib.reload(POM.CheckoutPage)

test_data = read_testdata("Testdata")
titles = read_testdata("Titles")
messages = read_testdata("Messages")

# @pytest.mark.skip
def test_demowebshop_1237(config):
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
    acnt.order_details(POM.CheckoutPage.order_num)
    verify_title(driver,titles["Orderdetailspage"])
    order = OrderDetailsPage(driver)
    order.smartphone()
    verify_title(driver,titles["Smartphonepage"])
    phone = SmartPhonePage(driver)
    phone.add_review()
    verify_title(driver,titles["Reviewpage"])
    review = ProductReviewPage(driver)
    review.review_title(test_data["Reviewtitle"])
    review.review_text(test_data["Reviewtext"])
    review.rating(int(test_data["Rating"]))
    review.submit_review()
    verify_title(driver, titles["Reviewpage"])
    review.verify_review(test_data["Firstname"])
    home.logout_link()
    verify_title(driver,titles["Homepage"])