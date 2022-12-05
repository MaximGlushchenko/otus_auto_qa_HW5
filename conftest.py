import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions




def pytest_addoption(parser):
    parser.addoption("--browser",
                     default="chrome")
    parser.addoption("--driver_folder",
                     default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--headless",
                     action="store_true")
    parser.addoption("--base_url",
                     default="http://192.168.0.74:8081")

@pytest.fixture
def main_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture
def admin_url(request):
    return request.config.getoption("--base_url") + "/admin"

@pytest.fixture
def catalog_url(request):
    return request.config.getoption("--base_url") + "/desktops"

@pytest.fixture
def registration_url(request):
    return request.config.getoption("--base_url") + "/index.php?route=account/register"

@pytest.fixture
def item_card_url(request):
    return request.config.getoption("--base_url") + "/tablet/samsung-galaxy-tab-10-1"




@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    headless = request.config.getoption("--headless")

    if _browser == "firefox" or _browser == "ff":
        options = FirefoxOptions()
        options.headless = headless
        driver = webdriver.Firefox(
            executable_path=f"{driver_folder}{os.sep}geckodriver", options=options
        )
    elif _browser == "chrome":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(
            executable_path=f"{driver_folder}{os.sep}chromedriver", options=options
        )
    elif _browser == "edge":
        options = EdgeOptions()
        options.headless = headless
        driver = webdriver.Edge(
            executable_path=f"{driver_folder}{os.sep}msedgedriver", options=options
        )
    elif _browser == "yandex":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(
            executable_path=f"{driver_folder}{os.sep}yandexdriver", options=options
        )
    elif _browser == "safari":
        driver = webdriver.Safari()

    driver.maximize_window()
    yield driver

    driver.close()
