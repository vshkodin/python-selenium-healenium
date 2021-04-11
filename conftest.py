from lib.common.base import Driver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path


def pytest_addoption(parser):
    parser.addoption("-H",action="store_true", default=False)
    parser.addoption("-I", action="store_true", default=False)
    parser.addoption("-L", action="store_true", default=False)
    parser.addoption('--base_url', action='store')



def pytest_sessionfinish(session, exitstatus):
    print('\n')
    if session.testsfailed:
        print("\n"*5)
        print(' |-------------------------------------|',"\n",
              '|                                     |',"\n",
              '|                                     |',"\n",
              f'|            !{session.testsfailed}!   Test Failures      |',"\n",
              '|                                     |',"\n",
              '|                ||                   |',"\n",
              '|                ||                   |',"\n",
              '|                ||                   |',"\n",
              r'|               \  /                  |',"\n",
              r'|                \/                   |',"\n",
              r'|                                     |',"\n",
              '|                                     |', "\n",
              '|_____________________________________|' )



@pytest.fixture()
def driver_init(request, headless, init_run):
    if headless:
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    driver.get(request.config.getoption("--base_url"))
    driver.implicitly_wait(15)
    driver.maximize_window()
    if init_run:
        driver.init_run = request.config.getoption("-I")
    driver.base_url = request.config.getoption("--base_url")
    driver=Driver(driver)
    yield driver
    driver.quit()

@pytest.fixture()
def HEALING(request):
    return request.config.getoption("-L")

@pytest.fixture()
def init_run(request):
    return request.config.getoption("-I")

@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture()
def headless(request):
    return request.config.getoption("-H")