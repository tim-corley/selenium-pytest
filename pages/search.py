"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:

    # URL

    URL = 'https://www.duckduckgo.com'

    # LOCATORS

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # INITIALIZER

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def search(self, term):
        # the '*' here expands the tuple variable being passed in into separate, positional args
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(term + Keys.RETURN)
