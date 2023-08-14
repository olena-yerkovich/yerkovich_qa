from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

product_locator = "div.catalog-products > ul > li.simple-slider-list__item.simple-slider-list__item_action.labeled.with-palette > div.simple-slider-list__link > a"
color_locator = "body > div.site-wrap > div.main-wrap.enabled_banner > div.content-wrap > div > div.product-page > div.new-product-item > div.product-item > div.product-item__buy > div.product-item__row > div.product-item__volume-select.with-palette > div > div.variants.scrolling.full-width > div:nth-child(7)"
buy_product_locator = "body > div.site-wrap > div.main-wrap.enabled_banner > div.content-wrap > div > div.product-page > div.new-product-item > div.product-item > div.product-item__buy > div.product-item__button > div"
added_product_qnt = "body>.site-wrap>.popup.cart>div>div.popup-content>div.cart-content-wrapper.scrolling>div.product-list-wrap>ul>li:first-child>.product-list_product-item>.product__column>.product__count-list>input[type=text]"
buy_product_wait_element = "body > div.site-wrap > div.popup.cart.ng-animate.ng-hide-animate > div > div.popup-content > div.cart-content-wrapper.scrolling > div.product-list-wrap > div.product-list__sidebar > div > div.button"

class BuyingProduct(BasePage):
     URL = "https://makeup.com.ua/ua/"
    
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
        
        # Go to the product
        product = self.driver.find_element(By.CSS_SELECTOR, product_locator)
        product.click()
        
        # Select variant (color)
        color_dropdown = self.driver.find_element(By.CLASS_NAME,"product-variant-selected")
        color_dropdown.click()

        color = self.driver.find_element(By.CSS_SELECTOR, color_locator)
        color.click()
        
        # Buy product
        buy_product = self.driver.find_element(By.CSS_SELECTOR, buy_product_locator)
        buy_product.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, buy_product_wait_element)))
        

    # Compare the products quantity in cart with expected products quantity
     def assert_compare_product_quantity(self, expected_quantity):
       product_quantity = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/ul/li/div[2]/div[1]/div[1]/input").get_attribute("value")
    
       assert product_quantity == expected_quantity

    # Compare the products color in cart with expected products color
     def assert_compare_product_color(self, expected_color):
        product_color = self.driver.find_element(By.CLASS_NAME,"product__header-option").text

        assert product_color == expected_color
   
    # Adding more products to cart
     def adding_product(self, n):
       add_more_products_btn = self.driver.find_element(By.CLASS_NAME,"product__button-increase")
       
       for i in range(n):
          add_more_products_btn = self.driver.find_element(By.CLASS_NAME, "product__button-increase")
          add_more_products_btn.click()
          WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, added_product_qnt), str(i + 2)))
 
    # Removing the added product from the cart
     def remove_product(self, n):
       remove_product_btn = self.driver.find_element(By.CLASS_NAME,"product__button-decrease")
       remove_product_btn.click()
       WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element_value((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/ul/li/div[2]/div[1]/div[1]/input"), n))
    
    # Deleting the product from the cart
     def delete_product(self):
        delete_btn = self.driver.find_element(By.CLASS_NAME,"product__button-remove")
        delete_btn.click()
        

        
     
       

