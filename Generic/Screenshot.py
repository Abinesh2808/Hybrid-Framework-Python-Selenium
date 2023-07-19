from datetime import datetime

def take_screenshot(driver):
    custom_format = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    driver.save_screenshot(f"../Screenshots/{custom_format}.png")