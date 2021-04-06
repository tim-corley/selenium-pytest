"""
This module contains ProductResultPage,
the page object for the Automation Practice product search result page
"""

from selenium.webdriver.common.by import By


class ProductResultPage:

    ALL_RESULTS = (By.CSS_SELECTOR, 'ul[class="product_list grid row"]')

    def __init__(self, browser):
        self.browser = browser

    def result_product_titles(self):
        result_titles = []
        products = self.browser.find_element(*self.ALL_RESULTS)
        items = products.find_elements(By.CSS_SELECTOR, 'div[class="product-container"]')
        for item in items:
            result_titles.append(item.find_element(By.TAG_NAME, 'h5'))
        return [item.text for item in result_titles]
