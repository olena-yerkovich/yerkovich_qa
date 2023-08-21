# Hello :) 
I'm Olena, Junior AQA Engineer, and this is my first project. Here you can find my API, database, and UI auto tests created by me. 
To get familiar with the structure of the framework, see the following sections.
# Framework structure
This framework consists of the 3 main folders: 
```
1. config 
2. modules 
3. tests
```

## Config

The __config__ folder contains the ___config.py___ file that we can use to set some configurations. 

## Modules
The __modules__ folder contains files with methods that are used in auto tests:
```   
1. api
2. common
3. ui
```
The __api__ folder contains files:
   - __init.py__
   - __github.py__ - contains GitHub class with main methods used in API auto tests

The __common__ folder contains:
   -  __init.py__
   -  __database.py__ - contains Database class with main methods used in database auto tests

The __ui__ folder contains:
   -  __init.py__
   -  __base_page.py__ - contains parent class 'BasePage' where we initialized the web driver
   -  __buying_product_individual.py__ - contains child class 'BuyingProduct' with all the methods that we use on particular page (makeup.com)
   -  __checkout_page_individual.py__ - contains child class 'CheckoutPage' with all the methods that we use on particular page (makeup.com)
   -  __sign_in_page.py__ - contains child class 'SignInPage' with all the methods that we use on particular page (github.com)
   -  __sign_in_page_individual.py__ - contains child class 'SignInPage_ind' with all the methods that we use on particular page (makeup.com)

## Tests
The __tests__ folder contains files with API, database, and UI auto tests:
```  
1. api
2. database
3. ui
```  
The __api__ contains:
   - __test_api.py__ - first API tests 
   - __test_fixtures.py__ - first API tests using fixtures 
   - __test_github_api.py__ - GitHub API tests 
   - __test_github_api_individual.py__ - GitHub API tests (created by me)
   - __test_http.py__ - first http requests tests 

The __database__ contains:
   - __test_database.py__ - database tests 
   - __test_database_individual.py__ - database tests (created by me)

The __ui__ contains:
   - __test_ui.py__ - first UI tests 
   - __test_ui_individual.py__ - UI tests (created by me)
   - __test_ui_page_object.py__ - UI tests using page object model 
___
There are 4 files that are also very important: 
1. __become_qa_auto.db__ - the database for testing 
2. __chromedriver.exe__ - the driver for UI testing
3. __conftest.py__ - the file that contains fixtures for all tests
4. __pytest.ini__ - the file that contains marks that we use to group tests by some common feature.

___
# Commands
To run the mandatory GitHub API tests use:
```
pytest -m api
```
To run individual GitHub API tests use:
```
pytest -m api_indi
```
To run mandatory database tests use:
```
pytest -m database
```
To run individual database tests use:
```
pytest -m database_indi
```
To run mandatory GitHub UI tests use:
```
pytest -m ui
```
To run individual (makeup.com) UI tests use:
```
pytest -m ui_indi
```
To run all the auto tests use:
```
pytest
```
