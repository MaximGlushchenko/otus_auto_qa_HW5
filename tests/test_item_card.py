from selenium.webdriver.common.by import By


def test_check_button_cart(browser, item_card_url):
    browser.implicitly_wait(0.5)
    browser.get(item_card_url)
    browser.find_element(By.CSS_SELECTOR, "#button-cart")


def test_check_input_quantity(browser, item_card_url):
    browser.implicitly_wait(0.5)
    browser.get(item_card_url)
    browser.find_element(By.CSS_SELECTOR, "#input-quantity")


def test_check_tweet_link(browser, item_card_url):
    browser.implicitly_wait(0.5)
    browser.get(item_card_url)
    browser.find_element(By.LINK_TEXT, "Tweet")


def test_check_add_to_wish_list_button(browser, item_card_url):
    browser.implicitly_wait(0.5)
    browser.get(item_card_url)
    browser.find_element(By.CSS_SELECTOR,
                         "button[type='button'][class='btn btn-default'][data-original-title='Add to Wish List']")


def test_check_compare_this_product_button(browser, item_card_url):
    browser.implicitly_wait(0.5)
    browser.get(item_card_url)
    browser.find_element(By.CSS_SELECTOR,
                         "button[type='button'][class='btn btn-default'][data-original-title='Compare this Product']")
