"""
These tests cover Automation Practice homepage
"""

import pytest
from pages.home import HomePage
from pages.search_result import ProductResultPage


def test_LogoDisplayed(browser):
    home_page = HomePage(browser)
    assert home_page.verify_logo_displayed()


def test_SearchReturnsValidResults(browser):
    term = 't-shirts'
    home_page = HomePage(browser)
    results_page = ProductResultPage(browser)
    home_page.product_search(term)
    assert term in results_page.result_product_titles()[0].lower()
