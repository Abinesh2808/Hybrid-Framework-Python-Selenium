from POM.HomePage import *
from POM.LoginPage import *
from POM.CellPhonesPage import *
from POM.SmartPhonePage import *
from POM.ShoppingCartPage import *
from POM.CheckoutPage import *
from Generic.Verify_Title import *
from Generic.ReadingExcel import *
import pytest

test_data = read_testdata("Testdata")
titles = read_testdata("Titles")
messages = read_testdata("Messages")

def test_demowebshop_1235(config):
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
    home.mouse_hover_electronics()
    home.cell_phones()
    verify_title(driver,titles["Cellphonespage"])
    cell_phone = CellPhonesPage(driver)
    cell_phone.smartphones()
    verify_title(driver,titles["Smartphonepage"])
    smartphone = SmartPhonePage(driver)
    smartphone.quantity(int(test_data["Quantity"]))
    smartphone.add_to_cart()
    smartphone.verify_product_added_to_cart_message(messages["Product Added to Cart"])
    smartphone.verify_cart_count(int(test_data["Quantity"]))
    smartphone.shopping_cart()
    verify_title(driver,titles["Cartpage"])
    cart = ShoppingCartPage(driver)
    cart.terms_and_conditions()
    cart.checkout_button()
    verify_title(driver,titles["Checkoutpage"])
    checkout = CheckOutPage(driver)
    checkout.country(test_data["Country"])
    checkout.city(test_data["City"])
    checkout.address1(test_data["Address1"])
    checkout.zip_code(int(test_data["Zipcode"]))
    checkout.phone_number(int(test_data["Phonenumber"]))
    checkout.billing_address_continue()
    checkout.shipping_address_continue()
    checkout.next_day_shipping_method()
    checkout.shipping_method_continue()
    checkout.credit_card()
    checkout.payment_method_continue()
    checkout.credit_card_type(test_data["Cardtype"])
    checkout.card_holder_name(test_data["Cardholdername"])
    checkout.card_number(int(test_data["Cardnumber"]))
    checkout.expiry_month("08")
    checkout.expiry_year("2030")
    checkout.car_code(int(test_data["Cardcode"]))
    checkout.payment_information_continue()
    checkout.confirm_button()
    verify_title(driver,titles["Checkoutpage"])
    checkout.verify_order(messages["Oder Placed"])
    checkout.verify_order_number()
    home.logout_link()
    verify_title(driver, titles["Homepage"])

