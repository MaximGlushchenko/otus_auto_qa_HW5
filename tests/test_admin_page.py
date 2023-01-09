from locators import *
from page_objects.AdminPage import AdminPage


def test_check_admin_page_elements(browser, base_url):
    admin_page = AdminPage(browser)
    admin_page.open(base_url)

    admin_page.element(AP_INPUT_USERNAME)
    admin_page.element(AP_INPUT_PASSWORD)
    admin_page.element(AP_FORGOTTEN_PASSWORD)
    admin_page.element(AP_OPEN_CART_LINK_TEXT)


def test_admin_add_product(browser, base_url):
    admin_page = AdminPage(browser)
    admin_page.admin_login(base_url)

    product_name = admin_page.admin_add_product()

    assert admin_page.element((By.CSS_SELECTOR, f'[alt="{product_name}"]'))
    assert admin_page.element(AP_ALERT_SUCCESS)

    admin_page.admin_del_product(product_name)


def test_admin_del_product(browser, base_url):
    admin_page = AdminPage(browser)
    admin_page.admin_login(base_url)

    product_name = admin_page.admin_add_product()

    admin_page.admin_del_product(product_name)

    assert admin_page.element_not_found((By.CSS_SELECTOR, f'[alt="{product_name}"]'))
    assert admin_page.element(AP_ALERT_SUCCESS)
