from Generic.Wrappers import *
from Generic.ReadData import *
from Generic.Logs import *

loc = read_locator("CellPhonesPage")
class CellPhonesPage:
    def __init__(self,driver):
        self.driver = driver

    def smartphones(self):
        log("info", "Clicking Smartphones")
        click_element(loc["Smartphone"],self.driver)
        log("info", "Smartphones Clicked")