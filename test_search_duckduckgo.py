import pytest
from selene import browser, be, have

@pytest.fixture
def browser_open():
    browser.open('https://duckduckgo.com/')
    browser.driver.maximize_window()
    yield
    print('Тест завершен')

def test_search_duckduckgo_1(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Переходите на DuckDuckGo. Бесплатно и надежно.'))


def test_search_duckduckgo_2(browser_open):
    browser.element('[name="q"]').should(be.blank).type('4578654398ghjfekghjhbnorenojrtio64564565nnoeщмщуцтще').press_enter()
    browser.element('html').should(have.text('результаты не найдены'))
    print('Поиск не дал результатов')

