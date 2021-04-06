"""
This module contains shared fixtures
"""

import json
import pytest
from selenium import webdriver


@pytest.fixture
def config(scope='session'):

    # read config file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config


@pytest.fixture()
def browser(config):
    if config['browser'] == 'Firefox':
        wd = webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        wd = webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument('headless')
        wd = webdriver.Chrome(options=opts)
    else:
        raise Exception(f'The "{config["browser"]}" browser is not supported')
    # set calls to wait for up to 10 seconds for elements
    wd.implicitly_wait(config['implicit_wait'])
    # resize browser window
    wd.maximize_window()
    wd.get(config['target_url'])
    # return the WebDriver instance for the setup
    yield wd
    # Quit the WebDriver instance for the cleanup
    wd.quit()
