import pytest
from selenium import webdriver
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import demoqa_tests.utils
from demoqa_tests.utils import *


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    demoqa_tests.utils.add_html(browser)
    demoqa_tests.utils.add_screenshot(browser)
    demoqa_tests.utils.add_logs(browser)
    demoqa_tests.utils.add_videos(browser)
