import pytest
from modules.api.clients.github import GitHub
from modules.common.database import Database
from modules.ui.page_objects.sign_in_page_individual import SignInPage_ind
from modules.ui.page_objects.buying_product_individual import BuyingProduct
from modules.ui.page_objects.checkout_page_individual import CheckoutPage

class User:
    
    def __init__ (self) -> None:
        self.name = None
        self.second_name = None
    def create (self):
        self.name = 'Olena'
        self.second_name = 'Yerkovich'
    def remove (self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

@pytest.fixture
def github_api():
    api = GitHub()

    yield api

@pytest.fixture
def db():
    db = Database()

    yield db

@pytest.fixture
def pagetest():
    pagetest = SignInPage_ind()

    yield pagetest

@pytest.fixture
def product_test():
    product_test= BuyingProduct()  

    yield product_test  
    
@pytest.fixture
def checkout_test():
    checkout_test = CheckoutPage()  

    yield checkout_test 