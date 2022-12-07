from selenium.webdriver.common.by import By


def test_check_top(browser, main_url):
    browser.implicitly_wait(0.5)
    browser.get(main_url)
    browser.find_element(By.CSS_SELECTOR, "#top")


def test_check_search(browser, main_url):
    browser.implicitly_wait(0.5)
    browser.get(main_url)
    browser.find_element(By.CSS_SELECTOR, "#search")


def test_check_menu(browser, main_url):
    browser.implicitly_wait(0.5)
    browser.get(main_url)
    browser.find_element(By.CSS_SELECTOR, "#menu")


def test_check_slideshow(browser, main_url):
    browser.implicitly_wait(0.5)
    browser.get(main_url)
    browser.find_element(By.CSS_SELECTOR, "#slideshow0")


def test_check_footer(browser, main_url):
    browser.implicitly_wait(0.5)
    browser.get(main_url)
    browser.find_element(By.CSS_SELECTOR, "footer")


def test_check_about(browser, main_url):
    browser.implicitly_wait(0.5)
    browser.get(main_url)
    browser.find_element(By.LINK_TEXT, "About Us")
