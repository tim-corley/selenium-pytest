"""
These tests cover DuckDuckGo searches
"""

import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


@pytest.mark.parametrize('term', ['panda', 'python', 'polar bear'])
def test_basic_search(browser, term):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given DuckDuckGo homepage is displayed
    search_page.load()

    # When user searches for a term
    search_page.search(term)

    # Then the search result query is the term
    assert term == result_page.search_value_input()

    # And the search result title contains the term
    assert term in result_page.title()
