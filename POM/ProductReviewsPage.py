from Generic.ReadData import *
from Generic.Wrappers import *
from Generic.Verify_Message import *
from Generic.Logs import *

loc = read_locator("ProductReviewPage")

class ProductReviewPage:
    def __init__(self,driver):
        self.driver = driver

    def review_title(self,rtitle):
        log("info", "Entering Review Title")
        enter_data(loc["Review Title"],rtitle,self.driver)
        log("info", "Review Title Entered")

    def review_text(self, rtext):
        log("info", "Entering Review Text")
        enter_data(loc["Review Text"],rtext,self.driver)
        log("info", "Review Text Entered")

    def rating(self,rate):
        log("info", "Clicking Specified Rating")
        self.driver.find_element("xpath",f"//input[@id='addproductrating_{rate}']").click()
        log("info", "Specified Rating Clicked")

    def submit_review(self):
        log("info", "Clicking Submit Review Button")
        click_element(loc["Submit Review"],self.driver)
        log("info", "Submit Review Button Clicked")

    def verify_review(self,name):
        try:
            lctn = self.driver.find_element("xpath",f"//span[contains(.,'{name}')]").location
            self.driver.execute_script(f"window.scrollBy({lctn['x']},{lctn['y']})")
            log("info", "Verifying Added Review")
            verify_message(self.driver,("xpath",f"//span[contains(.,'{name}')]"),name)
            log("info", "Added Review Verified")
        except:
            log("error", "Review Not Added")
            log("info", "Taking Screenshot")
            take_screenshot(self.driver)
            log("info", "Screenshot Captured")
            raise Exception("Review Not Added")



