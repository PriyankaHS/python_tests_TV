import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    activity_auto_label = (By.XPATH, "//td[@class='cart-item__details']/a")
    delete_item = (By.XPATH, "//a[@class='button button--tertiary']")
    cart_empty_msg = (By.XPATH, "//h1[contains(text(),'Your cart is empty')]")

    def verify_product_is_visible(self):
        return self.is_visible(self.activity_auto_label)

    def delete_an_item(self):
        self.click(self.delete_item)

    def cart_empty(self):
        time.sleep(5)
        assert self.is_displayed(self.cart_empty_msg)
