"""
These tests cover Automation Practice Login / Signup page
"""

import os
from dotenv import load_dotenv
from pages.auth import AuthPage
from pages.nav import HeaderNav


def test_UserLogin(browser):
    load_dotenv()
    username = os.getenv('USERNAME')
    nav = HeaderNav(browser)
    auth = AuthPage(browser)
    nav.navigate_to('signin')
    auth.input_login_credentials()
    auth.click_sigin_button()
    assert nav.verify_user_login(username)
