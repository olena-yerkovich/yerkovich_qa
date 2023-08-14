from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
     URL = "https://makeup.com.ua/ua/checkout/"

     def go_to_page(self):
        self.driver.get(CheckoutPage.URL)
    
     # Checkout the order 
     def checkout_product(self):
        checkout_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div[5]")
        checkout_btn.click()
