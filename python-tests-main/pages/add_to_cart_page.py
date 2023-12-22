import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.cart_page import CartPage


class AddToCart(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    add_to_cart_button = (By.XPATH, "//button[@name='add']")
    view_my_cart_button = (By.XPATH, "//a[@id='cart-notification-button']")
    plus_button = (By.XPATH, "//button[@name='plus']")
    buy_it_now_button = (By.XPATH, "//button[contains(text(),'Buy it now')]")
    check_out_button = (By.XPATH, "//button[@id='checkout']")
    sold_out = (By.XPATH, "//button[@name='add']")
    error_msg = (By.XPATH, "//span[@class='product-form__error-message']")

    def increase_quantity(self, qty):
        for i in range(qty):
            self.click(self.plus_button)

    def add_to_cart(self):
        self.click(self.add_to_cart_button)
        time.sleep(3)
        if self.is_displayed(self.error_msg):
            return None
        self.click(self.view_my_cart_button)
        time.sleep(5)
        return CartPage(self.driver)

    def verify_sold_out(self):
        return self.is_displayed(self.sold_out)

    def verify_error_msg(self):
        return self.is_displayed(self.error_msg)