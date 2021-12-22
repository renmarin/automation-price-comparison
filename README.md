# automation-price-comparison
Selenium automation script.

Script looks for product name on Amazon and BestBuy; collects: names, review counters and prices for search results; takes product with higher review counter on each site and comparing their prices.

Sometimes it is not possible to retrieve data for the check counters and therefore script needs to be restarted.

# Simulated user behavior
- user visits `amazon.com` website
- user fills out a search field with the product name and activates search ==>  
==> a page with search results is displayed.
- user looks for the product of specified color having maximum reviews count 
- user extracts minimum product price (with applied discount - if any) from the page
- user assigns `amazon_price` = product price
- user visits `bestbuy.com` website
- user chooses `United States` country
- user fills out a search field with the product name and activates search ==>  
==> a page with search results is displayed.
- user looks for the product of specified color having maximum reviews count 
- user extracts minimum product price (with applied discount - if any) from the page
- user assigns `bestbuy_price` = product price

# Prerequisites
Install everything from the requirements.txt file by executing the command: `pip install -r requirements.txt`

# How to run it
Use command in project directory to run test:
  - Mac/Linux users: `python3 -m pytest tests/test_shopping.py`
  - Windows users: `py -3 -m pytest tests/test_shopping.py`  

If encounter any problem use non-headless mode:
  `python3 tests/test_shopping.py`
  
