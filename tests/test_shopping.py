from selenium.webdriver.common.by import By


# extract data of items (name, review count, price) from search result page
def extract_data(driver, main_link, names_link, reviews_link, price_link, price_link_whole="", price_link_fracture=""):
    items_info = []
    all_items = [item for item in driver.find_elements(By.XPATH, main_link)]
    for item in all_items:
        try:
            name = item.find_element(By.XPATH, names_link).text
        except:
            name = "No name available"
        try:
            review = item.find_element(By.XPATH, reviews_link).text.strip('()').replace(',', '')
        except:
            review = "No review available"
        try:
            if price_link:
                price = item.find_element(By.XPATH, price_link).text
            else:
                price = item.find_element(By.XPATH, price_link_whole).text + "." + \
                        item.find_element(By.XPATH, price_link_fracture).text
        except:
            price = "No price available"
        if '$' in price:
            price = price.replace('$', '')
        item_info = [name, review, price]
        items_info.append(item_info)

    return items_info


# return product price for highest review count
def search_for_best_price(items_info, site, product):
    review = 0
    product_name = ""
    product_review = ""
    product_price = ""

    # choose one method
    for item in items_info:
        # print all items (for debug purposes)
        print(item)

        # method 1 | count only items with searched product name (Samsung Galaxy Buds Pro)
        # not best choice because item name can be valid but not same as product variable,
        # like: "Samsung - Galaxy Buds Pro"

        # if product in item[0] \
        #         and item[1] != "No review available" \
        #         and item[2] != "No price available" \
        #         and int(item[1]) > review:
        #     review = int(item[1])
        #     product_name = item[0]
        #     product_review = item[1]
        #     product_price = item[2]

        # method 2 | use all items
        # cons: product can have lots of review count but with different name
        # due to site's bad search engine

        if item[1] != "No review available" \
                and item[2] != "No price available" \
                and int(item[1]) > review:
            review = int(item[1])
            product_name = item[0]
            product_review = item[1]
            product_price = item[2]

    print(f"{site}_product_name: {product_name}")
    print(f"{site}_product_review: {product_review}")
    print(f"{site}_price: {product_price}")

    return product_price


def test_shopping(driver):
    product = 'Samsung Galaxy Buds Pro'
    color = 'Black'


    # Amazon

    driver.get('https://www.amazon.com/')

    search_box = driver.find_element(By.XPATH, ".//input[@name='field-keywords']")
    search_box.send_keys(product)
    search_box.submit()

    click_color = driver.find_element(By.XPATH, f".//a[@class='a-link-normal s-navigation-item'] [@title='{color}']//.//div[@class='colorsprite aok-float-left']")
    click_color.click()

    main_link = "//div[@class='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16']"
    names_link = ".//span[@class='a-size-medium a-color-base a-text-normal']"
    reviews_link = ".//span[@class='a-size-base']"
    price_link_whole = ".//span[@class='a-price-whole']"
    price_link_fracture = ".//span[@class='a-price-fraction']"

    items_info = extract_data(driver, main_link, names_link, reviews_link, None, price_link_whole, price_link_fracture)
    amazon_price = search_for_best_price(items_info, "Amazon", product)


    # BestBuy

    driver.get("https://www.bestbuy.com")
    driver.find_element(By.XPATH,"//a[@class='us-link']").click()

    # bypass BestBuy's pop-up window when first time enter it
    try:
        driver.find_element(By.XPATH, "//button[@class='c-close-icon c-modal-close-icon']").click()
    except:
        pass

    search_box = driver.find_element(By.XPATH, "//input[@id='gh-search-input']")
    search_box.click()
    search_box.send_keys(product)

    # added user_agent in conftest.py to work with headless mode
    search_box.submit()

    driver.find_element(By.XPATH, ".//input[@id='colorcat_facet-Black-0']").click()

    main_link = "//li[@class='sku-item']"
    names_link = ".//h4[@class='sku-header']"
    reviews_link = ".//span[@class='c-reviews-v4 c-reviews order-2']"
    price_link = ".//div[@class='priceView-hero-price priceView-customer-price']//span"

    items_info = extract_data(driver, main_link, names_link, reviews_link, price_link)
    bestbuy_price = search_for_best_price(items_info, "BestBuy", product)

    driver.quit()

    # once script completed the line below should be uncommented.
    assert amazon_price > bestbuy_price

# test/debug without headless mode
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    test_shopping(driver)
