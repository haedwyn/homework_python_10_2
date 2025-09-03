import uuid
from selene import browser, be, have

def test_search_request_has_result ():
    browser.open('/?hl=en')
    browser.element('[name="q"]').should(be.blank).type('wildberries').press_enter()
    browser.element('#search').should(be.visible)
    browser.all('#search a').first.should(have.attribute('href').containing('wildberries'))

def test_search_gibberish_shows_no_result ():
    browser.open('/?hl=en')
    gibberish = str(uuid.uuid4())
    browser.element('[name="q"]').should(be.blank).type(gibberish).press_enter()
    browser.element('#search').should(be.absent)
    browser.element('body').should(have.text('did not match any documents'))