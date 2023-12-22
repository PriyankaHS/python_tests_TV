import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestCart(BaseTest):
    driver: WebDriver

    @pytest.mark.browserstack
    def test_add_item(self):
        home_page = HomePage(self.driver)
        product_page = home_page.select_shopAll_button()
        add_to_cart_page = product_page.select_product()
        add_to_cart_page.increase_quantity(0)
        cart_page = add_to_cart_page.add_to_cart()
        assert cart_page.verify_product_is_visible()

    def test_sold_out(self):
        home_page = HomePage(self.driver)
        add_to_cart = home_page.search_product("2014")
        assert add_to_cart.verify_sold_out()

    def test_catalog(self):
        home_page = HomePage(self.driver)
        home_page.test_catalog()

    def test_search_product(self):
        home_page = HomePage(self.driver)
        add_to_cart_page = home_page.search_product("barbie and ken dolls")
        add_to_cart_page.increase_quantity(10)
        add_to_cart_page.add_to_cart()
        assert add_to_cart_page.verify_error_msg()

    def test_delete_product(self):
        home_page = HomePage(self.driver)
        product_page = home_page.view_product()
        add_to_cart_page = product_page.delete_product_from_cart()
        add_to_cart_page.increase_quantity(7)
        cart_page = add_to_cart_page.add_to_cart()
        cart_page.delete_an_item()

    def test_search_product_negative(self):
        home_page = HomePage(self.driver)
        add_to_cart_page = home_page.search_product("barbie and ken dolls")
        add_to_cart_page.increase_quantity(10)
        add_to_cart_page.add_to_cart()
        assert add_to_cart_page.verify_error_msg().__eq__(False)
