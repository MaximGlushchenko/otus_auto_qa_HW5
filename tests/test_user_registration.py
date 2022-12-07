from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_personal_details_registration(browser, registration_url):
    browser.get(registration_url)
    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-firstname")),
                                      message='"Input-firstname" element no found')
    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-lastname")),
                                      message='"Input-lastname" element no found')
    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-email")),
                                      message='"Input-email" element no found')
    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-telephone")),
                                      message='"Input-telephone" element no found')


def test_check_password_registration(browser, registration_url):
    browser.get(registration_url)
    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")),
                                      message='"Input-password" element no found')
    WebDriverWait(browser, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-confirm")),
                                      message='"Input-confirm" element no found')


def test_check_privacy_policy_link(browser, registration_url):
    browser.implicitly_wait(0.5)
    browser.get(registration_url)
    browser.find_element(By.LINK_TEXT, "Privacy Policy")


def test_check_login_button(browser, registration_url):
    browser.implicitly_wait(0.5)
    browser.get(registration_url)
    browser.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Continue'][class='btn btn-primary']")


def test_check_newsletter_subscribe_radiobutton_no(browser, registration_url):
    browser.implicitly_wait(0.5)
    browser.get(registration_url)
    browser.find_element(By.CSS_SELECTOR, "input[type='radio'][name='newsletter'][value='0']")


def test_check_newsletter_subscribe_radiobutton_yes(browser, registration_url):
    browser.implicitly_wait(0.5)
    browser.get(registration_url)
    browser.find_element(By.CSS_SELECTOR, "input[type='radio'][name='newsletter'][value='1']")
