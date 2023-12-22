import re
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.add_to_cart_page import AddToCart
from pages.base_page import BasePage
from pages.products_page import ProductPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    shop_all_button = (By.XPATH, "//a[contains(text(),'Shop all')]")
    search_button = (By.XPATH, "//summary[@aria-label='Search']/span")
    search_input = (By.XPATH, "//input[@id='Search-In-Modal']")
    click_first_product = (By.XPATH, "(//h3[@class='predictive-search__item-heading h5'])[1]")
    catalog = (By.LINK_TEXT, 'Catalog')
    product_text = (By.XPATH, "//span[text()='Catalog']")
    filter_text = (By.XPATH, "//h2[text()='Filter:']")
    availability = (By.XPATH, "//span[text()='Availability']/following-sibling::*[local-name()='svg']")
    reset = (By.XPATH, "//a[contains(text(),'Reset')]")
    view_all = (By.LINK_TEXT, "View all")
    price = (By.XPATH, "(//span[contains(text(),'Price')])[1]")
    price_from = (By.XPATH, "//input[@id='Filter-Price-GTE']")
    price_to = (By.XPATH, "//input[@id='Filter-Price-LTE']")
    price_filter = (By.XPATH, "(//span[text()='Rs. 500.00-Rs. 1,000.00'])[1]")
    price_list = (By.XPATH, "//span[contains(@class,'price-item price-item--regular')]")

    def select_shopAll_button(self):
        self.click(self.shop_all_button)
        return ProductPage(self.driver)

    def search_product(self, product_name):
        self.click(self.search_button)
        self.send_keys(self.search_input, product_name)
        time.sleep(3)
        self.click(self.click_first_product)
        return AddToCart(self.driver)

    def test_catalog(self):
        self.click(self.catalog)
        assert self.is_displayed(self.catalog).__eq__(True)
        assert self.is_displayed(self.filter_text)
        self.click(self.availability)
        time.sleep(3)
        assert self.is_displayed(self.reset).__eq__(True)

    def view_product(self):
        self.click(self.view_all)
        return ProductPage(self.driver)

    def test_price_range(self):
        self.click(self.catalog)
        self.click(self.price)
        self.send_keys(self.price_from, 500)
        self.send_keys(self.price_to, 1000)
        time.sleep(3)
        self.refresh_page()
        assert self.is_displayed(self.price_filter).__eq__(True)

    def test_price(self):
        self.click(self.catalog)
        self.click(self.price)
        self.send_keys(self.price_from, 500)
        self.send_keys(self.price_to, 1000)
        time.sleep(3)
        self.refresh_page()
        price_elements = self.find_elements(*self.price_list)
        price_outside_range = False

        for price_element in price_elements:
            price_text = price_element.text
            price_values = [float(val.replace(',', '').replace('Rs. ', '').strip()) for val in
                            re.findall(r'[\d,]+\.\d+', price_text)]
            if any(500 <= val <= 1000 for val in price_values):
                continue
            else:
                price_outside_range = True
                print(f"Price {price_values} is outside the range.")
        assert not price_outside_range, "One or more prices are outside the range (500 to 1000)."






