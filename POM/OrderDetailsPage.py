from Generic.Wrappers import *
from Generic.ReadingExcel import *
import os
from Generic.Screenshot import *
from Generic.Logs import *
from time import sleep

loc = read_locator("OrderDetailsPage")

class OrderDetailsPage:
    def __init__(self,driver):
        self.driver = driver

    def download_invoice(self):
        log("info", "Clicking Download Invoice Button")
        click_element(loc["PDF Invoice"],self.driver)
        log("info", "Download Invoice Button Clicked")
        sleep(1)

    def smartphone(self):
        log("info", "Clicking Smartphone")
        click_element(loc["Smartphone"],self.driver)
        log("info", "Smartphone Clicked")

    def verify_download(self,fname):
        try:
            log("info", "Verifying Download")
            os.chdir(r"C:\Users\Abinesh\Downloads")
            files = os.listdir()
            assert fname in files, "File Not Downloaded"
            log("info", "Download Verified")
        except:
            log("File Not Downloaded")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("File Not Downloaded")



