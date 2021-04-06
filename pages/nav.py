"""
This module contains HeaderNav,
the page object for the Automation Practice header navigation bar
"""

from selenium.webdriver.common.by import By


class HeaderNav:

    SIGN_IN = (By.CSS_SELECTOR, 'a[class="login"]')
    SIGN_OUT = (By.CSS_SELECTOR, 'a[class="logout"]')
    USERNAME = (By.CSS_SELECTOR, 'a[class="account"]')
    CONTACT = (By.ID, 'contact-link')

    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self, page):
        if page == 'signin':
            self.browser.find_element(*self.SIGN_IN).click()
        elif page == 'contact':
            self.browser.find_element(*self.CONTACT).click()
        elif page == 'logout':
            self.browser.find_element(*self.SIGN_OUT).click()

    def verify_user_login(self, username):
        username_display = self.browser.find_element(*self.USERNAME)
        return username_display.is_displayed() and username_display.text == username
