"""
This module contains shared fixtures
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    # initialize the ChromeBrowser instance
    b = selenium.webdriver.Chrome()
    # set calls to wait for up to 10 seconds for elements
    b.implicitly_wait(10)
    # return the WebDriver instance for the setup
    yield b
    # Quit the WebDriver instance for the cleanup
    b.quit()
