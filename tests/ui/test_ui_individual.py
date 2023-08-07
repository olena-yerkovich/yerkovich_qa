from modules.ui.page_objects.sign_in_page_individual import SignInPage_ind
from modules.ui.page_objects.sign_in_page_individual import BuyingProduct
from selenium.webdriver.common.by import By
import pytest
import time

# Testing the login functionality of the https://makeup.com.ua/ua
@pytest.mark.ui_indi
def test_check_login():
    pagetest = SignInPage_ind()

    pagetest.go_to_page()

    pagetest.login_to_page("olenka.yerkovich@gmail.com", "olenka123")
    
    pagetest.close()

# Finding and adding the product to the cart, comparing the product's name with the expected one
@pytest.mark.ui_indi
def test_compare_product_name():
    product_test = BuyingProduct()

    product_test.go_to_page()

    expected_product_name = "Maybelline New York SuperStay Matte Ink Liquid Lipstick"
    
    product_test.select_product(expected_product_name)

    product_name = product_test.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/ul/li/div[2]/div[1]/a/div[1]").text
    
    assert product_name == expected_product_name, f"Product name is incorrect! Expected: '{expected_product_name}', Actual: '{product_name}'"

    product_test.close()


# Checking if the product quantity in cart matches the expected quantity
@pytest.mark.ui_indi
def test_compare_product_quantity():
    product_test = BuyingProduct()

    product_test.go_to_page()

    product_test.select_product("Maybelline New York SuperStay Matte Ink Liquid Lipstick ")

    product_test.compare_product_quantity("1")

    product_test.close()

# Checking if the product variant in cart matches the variant that we've chosen previously
@pytest.mark.ui_indi
def test_product_variant():
    product_test = BuyingProduct()

    product_test.go_to_page()

    product_test.select_product("Maybelline New York SuperStay Matte Ink Liquid Lipstick ")

    color_dropdown = product_test.driver.find_element(By.CLASS_NAME,"product-variant-selected").text
    product_test.compare_product_color(color_dropdown)
    
    product_test.close()
    
# Adding more products and checking if the products quantity will be updated
@pytest.mark.ui_indi
def test_add_more_products():
    product_test = BuyingProduct()

    product_test.go_to_page()

    product_test.select_product("Maybelline New York SuperStay Matte Ink Liquid Lipstick ")

    product_test.adding_product(2)
    time.sleep(2)

    product_test.compare_product_quantity("3")

    product_test.close()


# Removing the added product from the cart and checking if the products quantity will be updated
@pytest.mark.ui_indi
def test_remove_product():
    product_test = BuyingProduct()

    product_test.go_to_page()

    product_test.select_product("Maybelline New York SuperStay Matte Ink Liquid Lipstick ")

    product_test.adding_product(2)
    time.sleep(3)

    product_test.compare_product_quantity("3")

    product_test.remove_product()
    time.sleep(3)

    product_test.compare_product_quantity("2")

    product_test.close()

    
# Checkout the order and checking if the product name is correct
@pytest.mark.ui_indi
def test_checkout_order_name():
    product_test = BuyingProduct()

    product_test.go_to_page()

    expected_product_name = "Maybelline New York SuperStay Matte Ink Liquid Lipstick"
    
    product_test.select_product(expected_product_name)

    product_test.checkout_product()

    product_name = product_test.driver.find_element(By.CLASS_NAME,"product__header").text

    assert product_name == expected_product_name

    product_test.close()


# Checkout the order and checking if the product variant is correct
@pytest.mark.ui_indi
def test_checkout_order_variant():
    product_test = BuyingProduct()

    product_test.go_to_page()

    product_test.select_product("Maybelline New York SuperStay Matte Ink Liquid Lipstick")

    product_test.adding_product(2)
    time.sleep(2)
    
    product_test.checkout_product()
    time.sleep(2)

    product_variant = product_test.driver.find_element(By.CLASS_NAME, "product__header-option").text
    
    product_test.compare_product_color(product_variant)
    
    product_test.close()



    
    