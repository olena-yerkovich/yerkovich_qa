from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"C:\Users\Lenovo\yerkovich_qa"
    DRIVER_NAME = "\chromedriver.exe"

    def __init__(self, driver=None):
        
        if driver  is not None:
            self.driver = driver
        
        else:
            self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
            )
    
    def close(self):
        self.driver.close()
