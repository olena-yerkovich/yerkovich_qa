from modules.ui.page_objects.sign_in_page_individual import SignInPage_ind
from modules.ui.page_objects.buying_product_individual import BuyingProduct
from modules.ui.page_objects.checkout_page_individual import CheckoutPage
from selenium.webdriver.common.by import By
import pytest


email = "olenka.yerkovich@gmail.com"
password = "olenka123"
product_name = "Maybelline New York SuperStay Matte Ink Liquid Lipstick"


# Testing the login functionality of the https://makeup.com.ua/ua
@pytest.mark.ui_indi
def test_check_login(pagetest):
    pagetest.go_to_page()
    pagetest.login_to_page(email, password)

# Finding and adding the product to the cart, comparing the product's name with the expected one
@pytest.mark.ui_indi
def test_compare_product_name(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    actual_product_name = product_test.driver.find_element(By.CSS_SELECTOR, "div[class*=product__header]").text
    
    assert actual_product_name == product_name, f"Product name is incorrect! Expected: '{product_name}', Actual: '{actual_product_name}'"
 
# Checking if the product quantity in cart matches the expected quantity
@pytest.mark.ui_indi
def test_compare_product_quantity(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    product_test.assert_compare_product_quantity("1")
    
# Checking if the product variant in cart matches the variant that we've chosen previously
@pytest.mark.ui_indi
def test_product_variant(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    color_dropdown = product_test.driver.find_element(By.CLASS_NAME,"product-variant-selected").text
    product_test.assert_compare_product_color(color_dropdown)
            
# Adding more products and checking if the products quantity will be updated
@pytest.mark.ui_indi
def test_add_more_products(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    product_test.adding_product(3)
    product_test.assert_compare_product_quantity("4")
    
# Removing the added product from the cart and checking if the products quantity will be updated
@pytest.mark.ui_indi
def test_remove_product(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    product_test.adding_product(2)
    product_test.assert_compare_product_quantity("3")
    product_test.remove_product("2")
    product_test.assert_compare_product_quantity("2")
       
# Checkout the order and checking if the product name is correct
@pytest.mark.ui_indi
def test_checkout_order_name(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    checkout_test = CheckoutPage(driver=product_test.driver)
    checkout_test.go_to_page()
    actual_product_name = product_test.driver.find_element(By.CLASS_NAME,"product__header").text

    assert actual_product_name == product_name
  
# Checkout the order and checking if the product variant is correct
@pytest.mark.ui_indi
def test_checkout_order_variant(product_test):
    product_test.go_to_page()
    product_test.select_product(product_name)
    product_test.adding_product(2)
    checkout_test = CheckoutPage(driver=product_test.driver)
    checkout_test.go_to_page()
    product_variant = checkout_test.driver.find_element(By.CLASS_NAME, "product__header-option").text
    product_test.assert_compare_product_color(product_variant)
    
    



    
    