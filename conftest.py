import pytest
from selene import browser

@pytest.fixture(autouse=True, scope='function')
def selene_setup():

    browser.config.base_url = 'https://www.google.com'
    browser.config.window_width = '1280'
    browser.config.window_height = '720'
    yield
    browser.quit()