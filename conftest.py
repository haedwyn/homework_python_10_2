import pytest
from selene import browser


@pytest.fixture(autouse=True, scope='function')
def selene_setup():
    # Упрощённая HTML-версия DuckDuckGo — стабильный DOM
    browser.config.base_url = 'https://html.duckduckgo.com'
    browser.config.timeout = 8
    browser.config.window_width = 1280
    browser.config.window_height = 900
    yield
    browser.quit()
