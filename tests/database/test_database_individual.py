import pytest
from modules.common.database import Database

# Getting all users (those who have orders and those who don't)
@pytest.mark.database_indi
def test_all_users_lef_join(db):
    u = db.get_users_lef_join()
    print(u)

    assert u[0][0] != 2
    assert u[1][0] == 2
    assert 'Sergii' in u[0][1] 
    assert 'stepan' not in u[1][1]


# Checking that database doesn't accept data with incorrect type (quantity should be int, not str). \
# NOTE!This test should NOT be passed successfully. Syntax error is expected.
@pytest.mark.database_indi
def test_product_insert_incorrect_type(db):
    db.insert_product( 17, 'печиво', 'солодке', '2 хлібини')
    water_qnt = db.select_product_qnt_by_id(17)
    
    print(water_qnt)
    
# Getting all customers whose name starts with 'Serg'
@pytest.mark.database_indi
def test_get_all_like_customers(db):
    db.insert_customer(23, 'Sergiy', 'someaddress', 'somecity', 'somecode','somecountry')
    u = db.get_like_customers('Serg')
    print(u)

    assert 'Serg' in u[0][1]
    assert 'Serg' in u[1][1]
    assert 'Serg' in u[2][1]

# Getting all customers with id in betweem 21 and 25
@pytest.mark.database_indi
def test_get_all_customers_by_between(db):
     u = db.get_customers_by_between(21, 25)
     print(u)

     assert u[0][0] in range (21, 25)
     assert u[1][0] in range (21, 25)

# Updating the products quantity and checking if database accepts correct data type
@pytest.mark.database_indi
def test_update_product_qnt(db):
    db.update_product_qnt_by_id(2, 30)
    quantity = db.select_product_qnt_by_id(2)
    print(quantity)

    assert quantity[0][0] == 30
    assert quantity[0][0] != '30'

# Creation of the new record in database and testing it's data
@pytest.mark.database_indi
def test_customers_data(db):
    db.insert_customer(44, 'Olena','','','','')
    u = db.get_customers_by_id(44)
    print(u)

    assert len(u) != 0
    assert len(u) == 1
    assert u[0][2] == ''
    assert u[0][2] != None


