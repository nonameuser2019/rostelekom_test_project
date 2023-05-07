import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print('Start browser chrome for test')
        options = Options()
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        driver.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print('Broser closed for test')
    driver.quit()
