import time

from selenium.webdriver.common.by import By

from pages.add_to_cart_page import AddToCart
from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    activity_auto_product = (By.XPATH, "//h3[contains(@id, 'product-grid-8002313486637')]/a")
    select_last_page = (By.XPATH, "//a[normalize-space()='34']")
    choose_drum = (By.XPATH, "//h3[contains(@id, 'product-grid-8002288877869')]/a")

    def select_product(self):
        self.click(self.activity_auto_product)
        return AddToCart(self.driver)

    def delete_product_from_cart(self):
        self.click(self.select_last_page)
        self.click(self.choose_drum)
        return AddToCart(self.driver)
