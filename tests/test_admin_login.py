from selenium.webdriver.common.by import By


def test_check_input_username(browser, admin_url):
    browser.implicitly_wait(0.5)
    browser.get(admin_url)
    browser.find_element(By.CSS_SELECTOR, "#input-username")


def test_check_input_password(browser, admin_url):
    browser.implicitly_wait(0.5)
    browser.get(admin_url)
    browser.find_element(By.CSS_SELECTOR, "#input-password")


def test_check_forgotten_password_link(browser, admin_url):
    browser.implicitly_wait(0.5)
    browser.get(admin_url)
    browser.find_element(By.LINK_TEXT, "Forgotten Password")


def test_check_login_button(browser, admin_url):
    browser.implicitly_wait(0.5)
    browser.get(admin_url)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit'][class='btn btn-primary']")


def test_check_opencart_link(browser, admin_url):
    browser.implicitly_wait(0.5)
    browser.get(admin_url)
    browser.find_element(By.LINK_TEXT, "OpenCart")
