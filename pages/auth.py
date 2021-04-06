"""
This module contains AuthPage,
the page object for the Automation Practice login / signup page
"""
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthPage:
    load_dotenv()
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'passwd')
    SIGNIN_BUTTON = (By.ID, 'SubmitLogin')
    USER_EMAIL = os.getenv('EMAIL')
    USER_PASSWORD = os.getenv('PASSWORD')

    def __init__(self, browser):
        self.browser = browser

    def input_login_credentials(self):
        email_input = self.browser.find_element(*self.EMAIL_INPUT)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        email_input.send_keys(self.USER_EMAIL + Keys.TAB)
        password_input.send_keys(self.USER_PASSWORD)

    def click_sigin_button(self):
        self.browser.find_element(*self.SIGNIN_BUTTON).click()

