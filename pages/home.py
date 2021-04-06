"""
This module contains HomePage,
the page object for the Automation Practice home page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePage:

    LOGO_IMAGE = (By.CSS_SELECTOR, 'img.logo')
    SEARCH_INPUT = (By.ID, 'search_query_top')
    CART_WIDGET = (By.CSS_SELECTOR, 'div.shopping_cart')
    HERO_SLIDER = (By.ID, 'slider_row')
    FEATURED_PRODUCTS = (By.ID, 'homefeatured')

    def __init__(self, browser):
        self.browser = browser

    def title(self):
        return self.browser.title

    def verify_logo_displayed(self):
        return self.browser.find_element(*self.LOGO_IMAGE).is_displayed()

    def product_search(self, term):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(term + Keys.RETURN)
