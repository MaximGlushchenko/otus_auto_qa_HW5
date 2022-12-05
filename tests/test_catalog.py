from selenium.webdriver.common.by import By


def test_check_list_view_button(browser, catalog_url):
    browser.implicitly_wait(0.5)
    browser.get(catalog_url)
    browser.find_element(By.CSS_SELECTOR, "#list-view")


def test_check_sort_by(browser, catalog_url):
    browser.implicitly_wait(0.5)
    browser.get(catalog_url)
    browser.find_element(By.CSS_SELECTOR, "#input-sort")


def test_check_show_limit(browser, catalog_url):
    browser.implicitly_wait(0.5)
    browser.get(catalog_url)
    browser.find_element(By.CSS_SELECTOR, "#input-limit")


def test_check_compare_total(browser, catalog_url):
    browser.implicitly_wait(0.5)
    browser.get(catalog_url)
    browser.find_element(By.CSS_SELECTOR, "#compare-total")


def test_check_laptops_notebooks_link_navbar(browser, catalog_url):
    browser.implicitly_wait(0.5)
    browser.get(catalog_url)
    browser.find_element(By.LINK_TEXT, "Laptops & Notebooks")
