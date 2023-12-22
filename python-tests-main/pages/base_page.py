from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ The purpose of a BasePage is to contain methods common to all page objects"""

    driver: WebDriver

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.find_element(*locator).send_keys(value)
        # self.find_element(*locator).clear()

    def clear(self, locator):
        self.find_element(locator).clear()

    def get_text(self, locator):
        return self.find_element(*locator).text()

    def get_title(self):
        """ Get the title of the current page. """
        return self.driver.title

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def wait_for_element(self, by_locator, timeout=10):
        """ Wait for an element to become visible before interacting with it. """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            return element
        except TimeoutException as e:
            raise TimeoutException(f"Element {by_locator} not found after {timeout} seconds. {e}")

    def is_displayed(self, locator):
        """
        Check if an element is displayed on the web page.
        Returns True if the element is displayed, False otherwise.
        """
        return self.find_element(*locator).is_displayed()

    def get_element_attribute(self, locator, attribute):
        """ Get the value of a specific attribute of an element. """
        self.find_element(*locator).get_attribute(attribute)

    def switch_to_frame(self, locator):
        """ Switch to an iframe using its locator. """
        self.driver.switch_to.frame(self.find_element(*locator))

    def switch_to_parent_frame(self):
        """ Switch back to the parent frame from the current iframe. """
        self.driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        """ Switch back to the default content from any iframe. """
        self.driver.switch_to.default_content()

    def wait_for_element_to_disappear(self, by_locator, timeout=10):
        """ Wait for an element to disappear from the page. """
        WebDriverWait(self.driver, timeout).until_not(EC.presence_of_element_located(by_locator))

    def go_back(self):
        """ Navigate the browser back to the previous page. """
        self.driver.back()

    def go_forward(self):
        """ Navigate the browser forward to the next page. """
        self.driver.forward()

    def get_url(self):
        """ Get the URL of the current page. """
        return self.driver.current_url

    def refresh_page(self):
        """ Refresh the current page. """
        self.driver.refresh()

    def accept_alert(self):
        """ Accept an alert dialog. """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """ Dismiss an alert dialog. """
        self.driver.switch_to.alert.dismiss()

    def get_all_cookies(self):
        """ Get all cookies on the current page. """
        return self.driver.get_cookies()

    def get_cookie(self, cookie_name):
        """ Get the value of a specific cookie by name. """
        return self.driver.get_cookie(cookie_name)

    def delete_cookie(self, cookie_name):
        """ Delete a specific cookie by name. """
        self.driver.delete_cookie(cookie_name)

    def delete_all_cookies(self):
        """ Delete all cookies on the current page. """
        self.driver.delete_all_cookies()

    def take_screenshot(self, filename='screenshot.png'):
        """ Take a screenshot of the current page. """
        self.driver.save_screenshot('./screenshots/' + filename)

    def scroll_to_element(self, locator):
        """ Scroll to a specific element identified by a locator. """
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_bottom_of_page(self):
        """ Scroll to the bottom of the entire page (not just the viewport). """
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top_of_page(self):
        """ Scroll to the top of the entire page (not just the viewport). """
        self.driver.execute_script("window.scrollTo(0, 0);")

    def navigate_to_url(self, url):
        """ Navigate to a URL using the browser's built-in navigation. """
        self.driver.get(url)

    def element_to_be_clickable(self, locator, timeout=10):
        """ Wait for an element to become clickable before interacting with it. """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return element
        except TimeoutException:
            raise TimeoutException(f"Element {locator} is not clickable after {timeout} seconds.")

    def double_click_element(self, locator):
        """Double-click on an element identified by a locator."""
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        actions.double_click(self.wait_for_element(locator)).perform()

    def right_click_element(self, locator):
        """ Right-click on an element identified by a locator. """
        from selenium.webdriver import ActionChains
        actions = ActionChains(self.driver)
        actions.context_click(self.wait_for_element(locator)).perform()
