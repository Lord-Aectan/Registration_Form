import pytest
from selene import browser


@pytest.fixture
def browser_start(scope='function'):
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()