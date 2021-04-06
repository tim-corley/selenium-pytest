"""
These tests cover DuckDuckGo searches
"""

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


def test_basic_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    TERM = 'baseball'

    # Given DuckDuckGo homepage is displayed
    search_page.load()

    # When user searches for "baseball"
    search_page.search(TERM)

    # Then the search result title contains "baseball"
    assert TERM in result_page.title()

    # And the search result query is "baseball"
    assert TERM == result_page.search_value_input()

    # And search result links pertain to "baseball"
    for title in result_page.result_link_titles():
        assert TERM.lower() in title.lower()

    raise Exception("Incomplete Test")
