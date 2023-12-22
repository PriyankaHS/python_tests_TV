import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType
from resources.test_data import TestData


@pytest.fixture(autouse=True)
def setup(request, getBrowser):
    if getBrowser == "chrome":
        options = Options()
        headless = request.config.getoption("--headless")
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif getBrowser == "safari":
        driver = webdriver.Safari()
    env = request.config.getoption("--env")
    TestData.set_environment(env)
    driver.get(TestData.url)
    # driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="class", autouse=True)
def getBrowser(request):
    browser = request.config.getoption("--crossBrowser")
    return browser


def pytest_addoption(parser):
    parser.addoption("--crossBrowser", action="store", default=TestData.browser)
    parser.addoption("--env", action="store", default=TestData.env)
    parser.addoption("--headless", action="store_true", default=False)


# Allure report hooks
@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(node, report):
    if report.failed:
        # Access the driver from the test class if available
        driver = getattr(node.cls, "driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            page_source = driver.page_source

            # Attach screenshot and page source to the report
            allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)
            allure.attach(page_source, name="page source", attachment_type=AttachmentType.HTML)
