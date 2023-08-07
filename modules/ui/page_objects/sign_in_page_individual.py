from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time


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

        time.sleep(2)
        # Find "login" btn
        login_button = self.driver.find_element(By.XPATH, "/html/body/form[1]/div/div/div[4]/button")
        login_button.click()
        
class BuyingProduct(BasePage):
     URL = "https://makeup.com.ua/ua/"

     def __init__(self) -> None:
        super().__init__()
    
     def go_to_page(self):
        self.driver.get(BuyingProduct.URL)

     def select_product(self, product):
         
        # Find the search field and click on it
        search_button = self.driver.find_element(By.CLASS_NAME,"search-button")
        search_button.click()

        # Search the product
        search_field = self.driver.find_element(By.ID,"search-input")
        search_field.send_keys(product)
        search_field.submit()
        time.sleep(5)
        
        # Go to the product
        product = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[1]/div/div[5]/ul/li[2]/div[2]/a")
        product.click()
        
        # Select variant (color)
        color_dropdown = self.driver.find_element(By.CLASS_NAME,"product-variant-selected")
        color_dropdown.click()

        color = self.driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div/div[2]/div[7]")
        color.click()
        time.sleep(2)
        
        # Buy product
        buy_product = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[1]")
        buy_product.click()
        time.sleep(3)
        

    # Compare the products quantity in cart with expected products quantity
     def compare_product_quantity(self, expected_quantity):
       product_quantity = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/ul/li/div[2]/div[1]/div[1]/input").get_attribute("value")
    
       assert product_quantity == expected_quantity

    # Compare the products color in cart with expected products color
     def compare_product_color(self, expected_color):
        product_color = self.driver.find_element(By.CLASS_NAME,"product__header-option").text

        assert product_color == expected_color
   
    # Adding more products to cart
     def adding_product(self, n):
       add_more_products_btn = self.driver.find_element(By.CLASS_NAME,"product__button-increase")
       
       for i in range(n):
          add_more_products_btn = self.driver.find_element(By.CLASS_NAME, "product__button-increase")
          add_more_products_btn.click()
          time.sleep(2)

       
    # Removing the added product from the cart
     def remove_product(self):
       remove_product_btn = self.driver.find_element(By.CLASS_NAME,"product__button-decrease")
       remove_product_btn.click()
    
    # Deleting the product from the cart
     def delete_product(self):
        delete_btn = self.driver.find_element(By.CLASS_NAME,"product__button-remove")
        delete_btn.click()
        
    # Checkout the order 
     def checkout_product(self):
        checkout_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/div[5]")
        checkout_btn.click()


        
     
       

