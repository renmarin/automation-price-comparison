# automation-price-comparison
Selenium automation script.

Script looks for product name on Amazon and BestBuy; collects: names, review counters and prices for search results; takes product with higher review counter on each site and comparing their prices.

Sometimes it is not possible to retrieve data for the check counters and therefore script needs to be restarted.

# Prerequisites
Install everything from the requirements.txt file by executing the command: `pip install -r requirements.txt`

# How to run it
To run test in use command in project directory:
  - Mac/Linux users: `python3 -m pytest tests/test_shopping.py`
  - Windows users: `py -3 -m pytest tests/test_shopping.py`  

If encounter any problem use non-headless mode:
  `python3 tests/test_shopping.py`
  
