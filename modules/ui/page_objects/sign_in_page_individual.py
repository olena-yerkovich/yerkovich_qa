from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage_ind(BasePage):
    URL = "https://makeup.com.ua/ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to_page(self):
        self.driver.get(SignInPage_ind.URL)

    def login_to_page(self, email, password):
        
        # Find the "login" icon and click on it
        login_icon = self.driver.find_element(By.CLASS_NAME, "header-office")
        login_icon.click()
   
        # Input email
        email_field = self.driver.find_element(By.ID, "login")
        email_field.click()
        email_field.send_keys(email)
        
        # Input password 
        pass_field = self.driver.find_element(By.ID, "pw")
        pass_field.click()
        pass_field.send_keys(password)

        # Find "login" btn
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[class*=full-width]")
        login_button.click()
        
