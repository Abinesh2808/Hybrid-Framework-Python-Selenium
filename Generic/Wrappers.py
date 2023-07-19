from Generic.Decorators import *

@verify_element
def enter_data(locator,data,driver):
    driver.find_element(*locator).send_keys(data)

@verify_element
def click_element(locator,driver):
    driver.find_element(*locator).click()

@verify_element
def clear_element(locator,driver):
    driver.find_element(*locator).clear()