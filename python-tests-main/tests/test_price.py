from pages.home_page import HomePage
from tests.base_test import BaseTest
from selenium.webdriver.remote.webdriver import WebDriver


class TestPrice(BaseTest):
    driver: WebDriver

    def test_price(self):
        home_page = HomePage(self.driver)
        home_page.test_price()

    def test_price_range(self):
        home_page = HomePage(self.driver)
        home_page.test_price_range()
