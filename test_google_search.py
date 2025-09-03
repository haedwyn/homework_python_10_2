from selene import browser, be, have
import uuid


def open_search():
    browser.open('/html/')
    return browser.element('input[name="q"]').should(be.visible)


def test_duckduckgo_html_positive():
    q = open_search()
    q.should(be.blank).type('qa.guru').press_enter()

    browser.element('#links').should(be.visible)
    # было: be.not_.empty  -> стало корректно для коллекций:
    browser.all('#links .result').should(have.size_greater_than(0))
    # дополнительная, более предметная проверка:
    browser.element('#links').should(have.text('qa.guru'))


def test_duckduckgo_html_negative_no_results():
    q = open_search()
    query = f'site:example.invalid {uuid.uuid4()}'
    q.should(be.blank).type(query).press_enter()

    # для «пусто» у коллекций используем have.empty
    browser.all('#links .result').should(have.size(0))  # или have.empty
    browser.element('body').should(have.no.text('example.invalid'))
